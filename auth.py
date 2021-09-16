import datetime

from aiogram import Bot, Dispatcher
from aiogram.utils.executor import Executor
from aiogram.contrib.fsm_storage.files import JSONStorage

from utils import scheduled

TOKEN = '1419134292:AAGr6LRmInyIlBrKSFX5FpEPnZHb3J2RwlE'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=JSONStorage('aiogram.json'))
runner = Executor(dp, skip_updates=True)

#runner.loop.create_task(scheduled.run_at(datetime.datetime(2020, 12, 31, 23, 59), scheduled.send_gifts(bot)))
