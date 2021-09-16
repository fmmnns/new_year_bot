from aiogram.types import CallbackQuery

from auth import dp
from ui import menus_text
from ui.inline import my_gifts_keyboard
import models
from user_states_group import UserStatesGroup


@dp.callback_query_handler(lambda query: query.data and query.data == 'my_gifts', state='*')
async def my_gifts(callback_query: CallbackQuery):
    db_user = models.get_user(callback_query.from_user)
    created_gifts = db_user.created_gifts

    if len(created_gifts) == 0:
        await callback_query.message.answer(menus_text.NO_GIFTS_CREATED)
        await callback_query.answer()
        await UserStatesGroup.default.set()
        return

    gifts_ids = models.get_gifts_ids(created_gifts)

    keyboard = my_gifts_keyboard.build(gifts_ids)
    await callback_query.message.answer(menus_text.GIFTS_LIST_MENU, reply_markup=keyboard)
    await callback_query.answer()
    await UserStatesGroup.default.set()
