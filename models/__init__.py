import os
from typing import List

from aiogram.types import User as TelegramUser
from aiogram.types import Message as TelegramMessage
from aiogram.types import Chat as TelegramChat
from peewee import *

from .base_model import BaseModel, DATABASE
from .user import User
from .chat import Chat
from .main_chat import MainChat
from .gift import Gift


def init():
    db = SqliteDatabase(DATABASE)
    db.create_tables([
        User,
        Chat,
        MainChat,
        Gift,
    ])


if not os.path.exists(DATABASE):
    init()


def get_user(telegram_user: TelegramUser) -> User:
    user, created = User.get_or_create(telegram_id=telegram_user.id)
    user.first_name = telegram_user.first_name
    user.last_name = telegram_user.last_name
    user.username = telegram_user.username
    user.save()
    return user


def get_chat(telegram_chat: TelegramChat) -> Chat:
    chat, created = Chat.get_or_create(telegram_id=telegram_chat.id)
    chat.title = telegram_chat.title
    chat.save()
    return chat


def get_gifts_ids(gifts) -> List[str]:
    gifts_ids = []
    for db_gift in gifts:
        gifts_ids.append(db_gift.id)
    return gifts_ids
