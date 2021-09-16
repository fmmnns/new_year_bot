from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from auth import dp
import models
from ui import menus_text
from ui.inline import menu_keyboard
from user_states_group import UserStatesGroup
from utils import logger


@dp.message_handler(lambda msg: msg.chat.id == msg.from_user.id, commands=['start', 'menu'], state='*')
@logger.log_msg
async def start(message: Message):
    models.get_user(message.from_user)
    models.get_chat(message.chat)

    keyboard = menu_keyboard.build()
    await message.answer(menus_text.MAIN_MENU,
                         reply_markup=keyboard)
    await UserStatesGroup.default.set()