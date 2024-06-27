from aiogram import types
from dispatcher import dp
from database.db import DataBase

@dp.message_handler(commands=["getchannels"])
async def get_channels(msg: types.Message):
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
        curl = channel[2]
        name = channel[3]

        text += "<b>{}. <a href='{}'>{}</a></b>\n".format(
            db_id, curl, name
        )
    
    await msg.answer(text)
