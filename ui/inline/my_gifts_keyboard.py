from typing import List

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def build(ids: List[str]) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=2)
    index = 1
    for id in ids:
        button = InlineKeyboardButton(text=str(index), callback_data='select_gift$' + str(id))
        keyboard.add(button)
        index += 1
    return keyboard
