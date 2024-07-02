import os

from aiogram import types
from dispatcher import dp, bot
from database.db import DataBase

@dp.message_handler(commands=["senddb"])
async def send_database(msg: types.Message):
    owners = DataBase().get_owners_id()
    user_id = msg.from_user.id

    if (user_id,) not in owners:
        return await msg.reply(
            "<b>вы не главный администратор!</b>"
        )

    database_file_path = os.path.join(
        os.path.dirname(__file__),
        "database/database.db"
    )

    try:
        with open(database_file_path, "rb") as file:
            await bot.send_document(
                chat_id=msg.chat.id,
                document=file,
                caption="Database"
            )
    except Exception as error:
        await msg.reply(
            "<b>{}</b>".format(
                error
            )
        )
