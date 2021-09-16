from aiogram.types import CallbackQuery

from auth import dp
from ui import menus_text
from ui.inline import my_gifts_keyboard, menu_keyboard
from user_states_group import UserStatesGroup
import models


@dp.callback_query_handler(lambda query: query.data and query.data.startswith('delete_gift'), state='*')
async def delete_gift(callback_query: CallbackQuery):
    gift_id = callback_query.data.split('$')[1]
    db_gift = models.Gift.get(id=gift_id)
    db_gift.delete_instance()

    db_user = models.get_user(callback_query.from_user)
    created_gifts = db_user.created_gifts

    if len(created_gifts) == 0:
        keyboard = menu_keyboard.build()
        await callback_query.message.answer(menus_text.MAIN_MENU, reply_markup=keyboard)
        await callback_query.message.delete_reply_markup()
        await UserStatesGroup.default.set()
        return

    gifts_ids = models.get_gifts_ids(created_gifts)

    keyboard = my_gifts_keyboard.build(gifts_ids)
    await callback_query.message.answer(menus_text.GIFTS_LIST_MENU, reply_markup=keyboard)
    await callback_query.message.delete_reply_markup()
    await UserStatesGroup.default.set()
