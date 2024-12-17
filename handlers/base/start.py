from aiogram.types import Message
from .inline_buttons import *
from .check_subscription import *
from dispatcher import dp, bot
from database.db import DataBase

db = DataBase()

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    channels = db.get_channels()

    subscribed_channels = []
    not_subscribed_channels = []

    for channel_id, name, link in channels:
        is_subscribed = await check_subscription(
            message.from_user.id,
            channel_id
        )
        if is_subscribed:
            subscribed_channels.append((channel_id, name, link))
        else:
            not_subscribed_channels.append((channel_id, name, link))

    keyboard = create_channel_buttons(not_subscribed_channels)

    if subscribed_channels:
        await message.reply("Вы уже подписаны на все каналы.")
    else:
        await message.reply(
            "Пожалуйста, подпишитесь на следующие каналы:",
            reply_markup=keyboard
        )

@dp.callback_query_handler(lambda c: c.data == 'check_subscription')
async def process_subscription_check(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    user_name = callback_query.from_user.full_name
    channels = db.get_channels()
    
    not_subscribed_channels = []
    all_subscribed = True

    for channel_id, name, link in channels:
        is_subscribed = await check_subscription(user_id, channel_id)
        if not is_subscribed:
            all_subscribed = False
            not_subscribed_channels.append((channel_id, name, link))

    keyboard = create_channel_buttons(not_subscribed_channels)

    if all_subscribed:
        await bot.send_message(
            user_id,
            "Вы уже подписаны на все каналы."
        )
        
        db.add_user(user_id, user_name)
        
        await bot.send_message(
            user_id,
            "Ваши данные успешно сохранены в базе."
        )
    else:
        await bot.send_message(
            user_id,
            "Пожалуйста, подпишитесь на следующие каналы:",
            reply_markup=keyboard
        )

