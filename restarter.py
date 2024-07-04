import os

from aiogram import types
from dispatcher import dp
from database.db import DataBase

@dp.message_handler(commands=["restart"])
async def restarter(msg: types.Message):
    admins_list = DataBase().get_admins_id()
    user_id = msg.from_user.id

    if (user_id,) not in admins_list:
        return

    os.system("python3 restart.py")
    await msg.answer("<b>Бот перезапущен</b>")
