from aiogram import types

def create_channel_buttons(channels, button_text="Я подписался"):
    buttons = [
        types.InlineKeyboardButton(
            text=name, url=link
        ) for _, name, link in channels
    ]
    buttons.append(
        types.InlineKeyboardButton(
            text=button_text,
            callback_data="check_subscription"
        )
    )
    
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard
