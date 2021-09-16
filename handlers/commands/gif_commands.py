from aiogram.types import Message, InputFile

from auth import dp, bot
from utils import logger
from utils.general import get_gif, get_full_name, try_delete


@dp.message_handler(commands=['eat', 'drink', 'beer', 'tea'], state='*')
@logger.log_msg
async def gif_commands(message: Message):
    variant = message.get_command(pure=True)
    chat_id = message.chat.id
    from_user = message.from_user

    gif = InputFile(get_gif(variant))

    await try_delete(message)

    text = ''
    if variant == 'eat':
        text = 'скушал вкусняшку'
    elif variant == 'drink':
        text = 'выпил watername'
    elif variant == 'beer':
        text = 'попил пива'
    elif variant == 'tea':
        text = 'выпил чаю'

    caption = get_full_name(from_user) + ' ' + text
    await bot.send_document(chat_id=chat_id, document=gif, caption=caption)
