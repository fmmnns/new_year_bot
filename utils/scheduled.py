import asyncio
import datetime
import math

from aiogram import Bot
from aiogram.types import ParseMode
from aiogram.utils.markdown import code
from peewee import fn

import models
from ui.inline import presents_keyboard
from utils.general import get_full_name


async def wait_until(dt):
    now = datetime.datetime.now()
    await asyncio.sleep((dt - now).total_seconds())


async def run_at(dt, coro):
    await wait_until(dt)
    return await coro


async def send_gifts(bot: Bot):
    gifts_count = len(models.Gift.select())
    users_count = len(models.User.select())
    max_gifts_for_user = math.ceil(gifts_count / (users_count - 1))
    for source_user in models.User.select():
        for gift in source_user.created_gifts:
            for target_user in models.User.select().order_by(fn.Random()):
                if target_user.telegram_id == source_user.telegram_id:
                    continue
                    pass

                if target_user.username == 'io1zl':
                    continue

                if len(target_user.received_gifts) >= max_gifts_for_user:
                    continue

                has_gift_from_user = False
                for received_gift in target_user.received_gifts:
                    if received_gift.from_user.telegram_id == source_user.telegram_id:
                        has_gift_from_user = True
                        break

                if has_gift_from_user:
                    continue

                gift.to_user = target_user
                gift.save()
                break

        for gift in source_user.created_gifts:
            for target_user in models.User.select().order_by(fn.Random()):
                if gift.to_user:
                    continue
                if target_user.username == 'io1zl':
                    continue
                if target_user.telegram_id == source_user.telegram_id:
                    continue
                    pass
                if len(target_user.received_gifts) >= max_gifts_for_user:
                    continue
                gift.to_user = target_user
                gift.save()
                break

    with open('static/ascii-yolka2.txt', 'r') as file:
        tree_text = file.read()

    for user in models.User.select():
        gifts_ids = models.get_gifts_ids(user.received_gifts)
        keyboard = presents_keyboard.build(gifts_ids)
        try:
            await bot.send_message(chat_id=user.telegram_id,
                                   text='С праздником пипятко!')
            await bot.send_message(chat_id=user.telegram_id,
                                   text=code(tree_text),
                                   parse_mode=ParseMode.MARKDOWN_V2,
                                   reply_markup=keyboard)
            print('send gift to {}'.format(str(user.first_name) + ' ' + str(user.last_name)))
            await asyncio.sleep(1)
        except Exception as e:
            print(e)
