from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher import State, StatesGroup
from database.db import DataBase
from dispatcher import dp
from config import owner_id

db = DataBase()

class AdminRemovalState(StatesGroup):
    admin_id = State()

@dp.message_handler(commands=['remove_admin'], state="*")
async def initiate_remove_admin(msg: types.Message):
    if msg.from_user.id != owner_id:
        return await msg.answer("У вас нет прав на удаление администратора.")
    
    await msg.answer("Введите ID администратора, которого хотите удалить:")
    await AdminRemovalState.admin_id.set()

@dp.message_handler(state=AdminRemovalState.admin_id)
async def get_admin_id(msg: Message, state: FSMContext):
    admin_id = msg.text
    
    if admin_id.isdigit():
        admin_id = int(admin_id)
        db.remove_admin(admin_id)
        await msg.answer(f"Администратор с ID {admin_id} был успешно удален.")
    else:
        await msg.answer("Пожалуйста, введите корректный числовой ID администратора.")
    
    await state.finish()
