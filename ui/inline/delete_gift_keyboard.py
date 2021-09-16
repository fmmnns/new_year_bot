from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def build(gift_id: str) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    delete_button = InlineKeyboardButton(text='Удалить', callback_data='delete_gift$' + gift_id)
    keyboard.add(delete_button)
    return keyboard
