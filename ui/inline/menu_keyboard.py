from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def build() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=2)
    make_gift_button = InlineKeyboardButton(text='Сделать подарок', callback_data='make_gift')
    my_gifts_button = InlineKeyboardButton(text='Мои подарки', callback_data='my_gifts')
    keyboard.add(make_gift_button)
    keyboard.add(my_gifts_button)
    return keyboard
