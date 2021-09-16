from aiogram.types import CallbackQuery

from auth import dp
import models
from utils.general import get_full_name


@dp.callback_query_handler(lambda query: query.data and query.data.startswith('open_gift'), state='*')
async def open_gift(callback_query: CallbackQuery):
    gift_id = callback_query.data.split('$')[1]
    db_gift = models.Gift.get(id=gift_id)

    reply_markup = callback_query.message.reply_markup
    inline_keyboard_row = reply_markup['inline_keyboard'][0]

    for index in range(0, len(inline_keyboard_row)):
        callback_data = inline_keyboard_row[index]['callback_data']
        current_gift_id = callback_data.split('$')[1]
        if current_gift_id == gift_id:
            inline_keyboard_row[index]['callback_data'] = 'opened_gift$' + gift_id
            inline_keyboard_row[index]['text'] = '🎉'

    await callback_query.answer()
    await callback_query.message.edit_reply_markup(reply_markup)

    await callback_query.message.answer(text='Пожелание от {}:\n{}'
                                        .format(get_full_name(db_gift.from_user), db_gift.text))

    print('{} открыл Подарок: пожелание от {}:\n{}'
          .format(str(callback_query.from_user.first_name) + str(callback_query.from_user.last_name),
                  get_full_name(db_gift.from_user),
                  db_gift.text))