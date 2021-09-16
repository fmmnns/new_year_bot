from aiogram.types import Message

from auth import dp
from user_states_group import UserStatesGroup
import models
from ui import menus_text
from ui.inline import menu_keyboard
from utils import logger


@dp.message_handler(state=UserStatesGroup.wait_gift)
@logger.log_msg
async def make_gift(message: Message):
    db_user = models.get_user(message.from_user)

    gift_text = message.text
    models.Gift.create(from_user=db_user, text=gift_text)

    keyboard = menu_keyboard.build()
    await message.answer(menus_text.GIFT_SAVED)
    await message.answer(menus_text.MAIN_MENU, reply_markup=keyboard)
    await UserStatesGroup.default.set()
