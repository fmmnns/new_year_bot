from typing import List

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def build(gift_ids: List[str]) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=10)
    for id in gift_ids:
        gift_button = InlineKeyboardButton('🎁', callback_data='open_gift$' + str(id))
        keyboard.insert(gift_button)
    return keyboard
