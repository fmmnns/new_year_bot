from aiogram.types import Message, ParseMode
from aiogram.utils.markdown import code

from auth import dp, bot
from utils import logger
from utils.general import try_delete


@dp.message_handler(commands=['snow', 'snegovik', 'yolka'], state='*')
@logger.log_msg
async def ascii_commands(message: Message):
    variant = message.get_command(pure=True)
    with open('static/ascii-{}.txt'.format(variant), 'r') as file:
        snow_text = file.read()

    chat_id = message.chat.id
    await try_delete(message)
    await bot.send_message(chat_id=chat_id, text=code(snow_text), parse_mode=ParseMode.MARKDOWN_V2)

