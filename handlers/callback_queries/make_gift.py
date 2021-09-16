from aiogram.types import CallbackQuery

from auth import dp
import models
from ui import menus_text
from user_states_group import UserStatesGroup


@dp.callback_query_handler(lambda query: query.data and query.data == 'make_gift', state='*')
async def make_gift(callback_query: CallbackQuery):
    await callback_query.message.answer(menus_text.MAKE_GIFT_INVITE)
    await callback_query.answer()
    await UserStatesGroup.wait_gift.set()
