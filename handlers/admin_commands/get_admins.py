from aiogram import types
from dispatcher import dp
from database.db import DataBase

@dp.message_handler(commands=["getadmins"])
async def get_admins(msg: types.Message):
    admins_list = DataBase().get_admins_id()
    user_id = msg.from_user.id

    if (user_id,) in admins_list:
        pass
    else:
        return
    
    text = (
        "<b>Admins list:\n</b>"
    )

    for admin in admins_list:
        db_uid = user[0]
        admin_id = user[1]
        name = user[2]

        text += "{}. <a href='tg://user?id={}'>{}</a>".format(
            db_uid, admin_id, name
        )
    
    await msg.answer(text)
