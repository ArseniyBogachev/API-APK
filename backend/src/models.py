import ormar
from .db import metadata, database


class FileAndKeys(ormar.Model):
    class Meta:
        metadata = metadata
        database = database

    id: int = ormar.Integer(primary_key=True)
    title: str = ormar.String(max_length=20)
    api_keys: str = ormar.JSON()
