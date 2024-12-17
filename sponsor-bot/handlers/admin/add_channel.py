from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher import State, StatesGroup
from database.db import DataBase
from dispatcher import dp

db = DataBase()

class ChannelState(StatesGroup):
    channel_id = State()
    channel_name = State()
    channel_link = State()

@dp.message_handler(commands=['add_channel'], state="*")
async def initiate_add_channel(msg: Message):
    await mssg.answer("Введите ID канала:")
    await ChannelState.channel_id.set()

@dp.message_handler(state=ChannelState.channel_id)
async def get_channel_id(msg: Message, state: FSMContext):
    channel_id = msg.text
    
    if channel_id.isdigit():
        channel_id = int(channel_id)
    else:
        await start_add_channel(msg)
    
    await state.update_data(channel_id=channel_id)
    await msg.answer("Введите имя канала:")
    await ChannelState.next()

@dp.message_handler(state=ChannelState.channel_name)
async def get_channel_name(msg: Message, state: FSMContext):
    await state.update_data(channel_name=msg.text)
    await msg.answer("Введите ссылку на канал:")
    await ChannelState.next()

@dp.message_handler(state=ChannelState.channel_link)
async def get_channel_link(msg: Message, state: FSMContext):
    data = await state.get_data()
    db.add_channel(
        channel_id=int(data.get('channel_id')),
        channel_name=data.get('channel_name'),
        channel_link=message.text
    )

    await message.answer("Канал добавлен успешно!")
    await state.finish()

