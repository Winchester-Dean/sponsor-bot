from aiogram import types
from dispatcher import dp
from database.db import DataBase

@dp.message_handler(commands=["getusers"])
async def get_users_list(msg: types.Message):
    admins_list = DataBase().get_admins_id()
    from_id = msg.from_user.id

    if (from_id,) not in admins_list:
        return await msg.reply(
            "<b>Вы не администратор!</b>"
        )
    
    text = (
        "<b>Users list:\n</b>"
    )

    users_list = DataBase().get_users()
    for user in users_list:
        dbid = user[0]
        user_id = user[1]
        name = user[2]
        username = user[3]

        text += "<b>{}. <a href='tg://user?id={}'>{}</a>: {}\n</b>".format(
            dbid, user_id, name, username
        )

    await msg.answer(text)

