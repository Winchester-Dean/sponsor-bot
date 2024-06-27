from aiogram import types
from dispatcher import dp
from database.db import DataBase

@dp.message_handler(commands=["addadmin"])
async def add_new_admin(msg: types.Message, state=None):
    args = msg.text.split()
    admins_list = DataBase().get_admins_id()
    user_id = msg.from_user.id

    if (user_id,) in admins_list:
        pass
    else:
        return
    
    if len(args) > 3:
        await msg.answer("<b>Error</b>")
    else:
        pass

    if args[1].isdigit():
        adm_id = int(args[1])
    else:
        await msg.answer("<b>Ошибочный айди</b>")

    DataBase().add_new_admin(adm_id, args[2])
    await msg.answer("<b>Новый администратор записан в базу данных</b>")
