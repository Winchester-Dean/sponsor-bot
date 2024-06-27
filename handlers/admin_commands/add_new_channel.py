from aiogram import types
from dispatcher import types
from database.db import DataBase

@dp.message_handler(commands=["addnew"])
async def add_channel(msg: types.Message):
    args = msg.text.split()
    admins_list = DataBase().get_admins_id()
    user_id = msg.from_user.id

    if (user_id,) in admins_list:
        pass
    else:
        return
    
    if len(args) > 3:
        return await msg.answer("<b>Error</b>")
    else:
        pass
    
    if args[1].isdigit():
        channel_id = int(args[1])
    else:
        return await msg.answer("<b>Invalid id</b>")
    
    DataBase().add_new_channel(
        channel_id, args[2], args[3]
    )
    await msg.answer("<b>Новый канал успешно добавлен в базу!</b>")
