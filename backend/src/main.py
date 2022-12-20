import os
import subprocess
from fastapi import FastAPI, UploadFile, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from .utils import SearchApiKeys

app = FastAPI()


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
        await websocket.send_text('100')
        await websocket.send_json(keys)
    except:
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