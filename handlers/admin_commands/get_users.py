from aiogram import types
from dispatcher import dp
from database.db import DataBase

@dp.message_handler(commands=["getusers"])
async def get_users(msg: types.Message):
    admins_list = DataBase().get_admins_id()
    user_id = msg.from_user.id

    if (user_id,) in admins_list:
        pass
    else:
        return
    
    text = (
        "<b>Users list:\n</b>"
    )

    users_list = DataBase().get_users()
    for user in users_list:
        db_uid = user[0]
        user_id = user[1]
        name = user[2]

        text += "<b>{}. <a href='tg://user?id={}'>{}</a></b>\n".format(
            db_uid, user_id, name
        )
    
    await msg.answer(text)
