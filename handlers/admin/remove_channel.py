from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher import State, StatesGroup
from database.db import DataBase
from dispatcher import dp
from config import owner_id

db = DataBase()

class ChannelRemovalState(StatesGroup):
    channel_id = State()

@dp.message_handler(commands=['remove_channel'], state="*")
async def initiate_remove_channel(msg: Message):
    if msg.from_user.id != owner_id:
        return await msg.answer("У вас нет прав на удаление канала.")
    
    await msg.answer("Введите ID канала, который хотите удалить:")
    await ChannelRemovalState.channel_id.set()

@dp.message_handler(state=ChannelRemovalState.channel_id)
async def get_channel_id(msg: Message, state: FSMContext):
    channel_id = msg.text
    
    if channel_id.isdigit():
        channel_id = int(channel_id)
        db.remove_channel(channel_id)
        await msg.answer(f"Канал с ID {channel_id} был успешно удален.")
    else:
        await msg.answer("Пожалуйста, введите корректный числовой ID канала.")
    
    await state.finish()
