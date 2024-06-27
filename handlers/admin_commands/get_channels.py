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
        "<b>Channels list:\n</b>"
    )

    channels = DataBase().get_channels()
    for channel in channels:
        db_id = channel[0]
        chid = channel[1]
        curl = channel[2]
        name = channel[3]

        text += "{}. <a href='{}'>{}</a>: `{}`".format(
            db_id, curl, name, chid
        )
    
    await msg.answer(text)
