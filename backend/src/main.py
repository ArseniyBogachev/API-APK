import os
import subprocess
import json
import shutil
from .db import metadata, database, engine
from fastapi import FastAPI, UploadFile, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from .utils import SearchApiKeys
from .models import *


app = FastAPI()
metadata.create_all(engine)
app.state.database = database


@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    filename = await websocket.receive_text()

    base_dir = os.path.abspath(os.curdir)
    try:
        await websocket.send_text('10')
        os.chdir(os.path.join(base_dir, 'apktool'))
        subprocess.call(['apktool.bat', 'd', f'../apk_save/{filename}', '-f'])

        await websocket.send_text('65')
        search = SearchApiKeys(filename, websocket)
        keys = await search.get_keys()

        os.chdir(base_dir)
        shutil.rmtree(os.path.join(base_dir, 'apktool', filename[:-4]), ignore_errors=True)
        os.remove(os.path.join(base_dir, 'apk_save', filename))
        await websocket.send_json(keys)

        keys_json = json.dumps(keys)
        await FileAndKeys.objects.create(title=filename, api_keys=keys_json)
    except Exception:
        raise FileNotFoundError('Error')
    finally:
        os.chdir(base_dir)


@app.post("/upload/")
async def upload(file: UploadFile):
    if file.filename[-3:] != 'apk':
        raise FileNotFoundError('File extension must be: \'apk\'')

    path_apk = os.path.join(os.path.abspath(os.curdir), 'apk_save', file.filename)
    with open(path_apk, 'wb') as f:
        f.write(bytes(file.file.read()))

    return file.filename
