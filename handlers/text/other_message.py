from aiogram.types import Message

from auth import dp
from user_states_group import UserStatesGroup
from utils import logger


@dp.message_handler(state=UserStatesGroup.default)
@logger.log_msg
async def other_message(message: Message):
    pass
