from peewee import *

from .base_model import BaseModel
from .chat import Chat


class MainChat(BaseModel):
    id = AutoField()
    chat = ForeignKeyField(Chat)
