from peewee import *

from .base_model import BaseModel


class Chat(BaseModel):
    telegram_id = BigIntegerField(primary_key=True)
    title = CharField(null=True)
