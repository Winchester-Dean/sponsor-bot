from database.db import DataBase
from aiogram import types
from dispatcher import dp, bot

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

buttons = []

channels = DataBase().get_channels()
for channel in channels:
    buttons.append(
        InlineKeyboardButton(
            text=channel[3],
            url=channel[2]
        )
    )

inline_buttons = InlineKeyboardMarkup(row_width=1)
inline_buttons.add(*buttons)
inline_buttons.add(
    InlineKeyboardButton(
        text="Agza boldym", callback_data="agza"
    )
)

device_buttons = [
    KeyboardButton(
        text="iOS ucin"
    ),
    KeyboardButton(
        text="Android ucin"
    )
]
dbuttons = ReplyKeyboardMarkup(resize_keyboard=True)
dbuttons.add(*device_buttons)

async def check_sub(bot, user_id):
    channels_ids = DataBase().get_channels_id()
    for channel_id in channels_ids:
        status = await bot.get_chat_member(
            f"-100{channel_id[0]}", user_id
        )

        if status["status"] != "left":
            return True
        else:
            return False

@dp.message_handler(commands=["start"])
async def start_handler(msg: types.Message):
    user_id = msg.from_user.id
    users = DataBase().get_users_id()

    if (user_id,) not in users:
        DataBase().add_new_user(
            user_id, msg.from_user.first_name
        )
    else:
        pass

    check = await check_sub(bot, user_id)
    if check:
        await msg.answer(
            "Maladis siz agza bolypsynyz. Haysy kod gerek?",
            reply_markup=dbuttons
        )
    else:
        await msg.answer(
            "<b>Salam taze bet kody alasyn gelse kanallara agza bol:</b>",
            reply_markup=inline_buttons
        )

@dp.callback_query_handler(text="agza")
async def send_code(call: types.CallbackQuery):
    status = await check_sub(bot, call.from_user.id)
    if status:
        await call.message.answer(
            "Maladis siz agza bolypsynyz. Haysy kod gerek?",
            reply_markup=dbuttons
        )
    else:
        await call.message.answer(
            "Siz agza bolmansynyz!",
            reply_markup=inline_buttons
        )
