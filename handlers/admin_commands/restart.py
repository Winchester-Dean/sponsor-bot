from aiogram import types
from dispatcher import dp
from database.db import DataBase

from restart import restart

@dp.message_handler(commands=["restart"])
async def restart_handler(msg: types.Message):
    admins_list = DataBase().get_admins_id()
    user_id = msg.from_user.id

    if (user_id,) not in admins_list:
        return await msg.reply(
            "<b>вы не администратор!</b>"
        )
    
    await msg.answer("<b>Перезапуск запущен!</b>")

    try:
        restart()
    except Exception as error:
        return await msg.answer(f"<b>{error}</b>")
    await msg.answer("<b>Бот перезапущен!</b>")
