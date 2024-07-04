from aiogram import types
from dispatcher import dp
from database.db import DataBase

@dp.message_handler(commands=["getchannels"])
async def get_channels_list(msg: types.Message):
    admins_list = DataBase().get_admins_id()
    user_id = msg.from_user.id

    if (user_id,) not in admins_list:
        return await msg.reply(
            "<b>Вы не администратор!</b>"
        )

    text = (
        "<b>Channels list:\n</b>"
    )

    channels = DataBase().get_channels()
    for channel in channels:
        dbid = channel[0]
        channel_id = channel[1]
        curl = channel[2]
        name = channel[3]

        text += "{}. <a href='{}'>{}</a>:\n<code>{}</code>\n".format(
            dbid, curl, name, channel_id
        )

    await msg.answer(text)

