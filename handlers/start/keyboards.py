from database.db import DataBase

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

inline_buttons = InlineKeyboardMarkup()
inline_buttons.add(*buttons)
inline_buttons.add(
    InlineKeyboardButton(
        text="Agza boldym",
        callback_data="agza"
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
