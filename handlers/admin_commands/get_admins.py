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

    admins = DataBase().get_admins()
    for admin in admins:
        db_uid = admin[0]
        admin_id = admin[1]
        name = admin[2]

        text += "<b>{}. <a href='tg://user?id={}'>{}</a></b>\n".format(
            db_uid, admin_id, name
        )
    
    await msg.answer(text)
