from aiogram import types
from dispatcher import dp, bot
from database.db import DataBase

from handlers.start.check_sub import checksub
from handlers.start.keyboards import inline_buttons, dbuttons

@dp.message_handler(commands=["start"])
async def start_handler(msg: types.Message):
    users = DataBase().get_users_id()
    user_id = msg.from_user.id

    if (user_id,) not in users:
        DataBase().new_user(
            user_id,
            msg.from_user.first_name,
            msg.from_user.username
        )
    
    check = await checksub(bot, user_id)
    if check:
        return await msg.answer(
            "<b>Maladis siz agza bolypsynyz. Haysy kod gerek?</b>",
            reply_markup=dbuttons
        )
    else:
        return await msg.answer(
            "<b>Salam taze bet kody alasyn gelse kanallara agza bol:</b>",
            reply_markup=inline_buttons
        )

@dp.callback_query_handler(text="agza")
async def send_code(call: types.CallbackQuery):
    status = await check_sub(bot, call.from_user.id)
    if status:
        await call.message.answer(
            "<b>Maladis siz agza bolypsynyz. Haysy kod gerek?</b>",
            reply_markup=dbuttons
        )
    else:
        await call.message.answer(
            "<b>Siz agza bolmansynyz!</b>",
            reply_markup=inline_buttons
        )
