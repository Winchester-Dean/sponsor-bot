from aiogram import types
from dispatcher import dp
from database.db import DataBase

@dp.message_handler(commands=["addadmin"])
async def new_admin(msg: types.Message):
    args = msg.text.split(maxsplit=2)
    owners = DataBase().get_owners_id()
    user_id = msg.from_user.id

    if (user_id,) not in owners:
        return await msg.reply(
            "<b>Вы не главный администратор!</b>"
        )

    if len(args) == 3:
        pass
    else:
        await msg.reply("<b>Error</b>")

    if args[1].isdigit():
        admin_id = int(args[1])
    else:
        return await msg.reply("<b>Invalid id</b>")

    try:
        DataBase().new_admin(
            admin_id, args[2]
        )
    except Exception as error:
        await msg.asnwer(
            "<b>{}</b>".format(
                error
            )
        )

    await msg.answer(
        "<b>Новый администратор записан в базу!</b>"
    )

