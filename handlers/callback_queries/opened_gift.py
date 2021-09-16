from aiogram.types import CallbackQuery

from auth import dp


@dp.callback_query_handler(lambda query: query.data and query.data.startswith('opened_gift'), state='*')
async def opened_gift(callback_query: CallbackQuery):
    await callback_query.answer('🎈')
