from aiogram.types import CallbackQuery

from auth import dp
from ui import menus_text
from ui.inline import delete_gift_keyboard
from user_states_group import UserStatesGroup
import models


@dp.callback_query_handler(lambda query: query.data and query.data.startswith('select_gift'), state='*')
async def select_gift(callback_query: CallbackQuery):
    gift_id = callback_query.data.split('$')[1]

    try:
        db_gift = models.Gift.get(id=gift_id)
    except models.gift.DoesNotExist:
        await callback_query.answer(menus_text.GIFT_IS_NOT_EXISTS)
        await UserStatesGroup.default.set()
        return

    keyboard = delete_gift_keyboard.build(gift_id)
    await callback_query.message.answer(db_gift.text, reply_markup=keyboard)
    await callback_query.answer()
    await UserStatesGroup.default.set()
