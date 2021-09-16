from peewee import *

from .base_model import BaseModel
from .user import User


class Gift(BaseModel):
    id = AutoField()
    from_user = ForeignKeyField(User, backref='created_gifts')
    to_user = ForeignKeyField(User, backref='received_gifts', null=True)
    text = TextField()
    picture_path = CharField(max_length=255, null=True)
