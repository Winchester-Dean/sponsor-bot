from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher import State, StatesGroup
from database.db import DataBase
from dispatcher import dp
from config import owner_id

db = DataBase()

class AdminState(StatesGroup):
    admin_id = State()
    admin_name = State()
    admin_contact = State()

@dp.message_handler(commands=['add_admin'], state="*")
async def initiate_add_admin(msg: Message):
    if msg.from_user.id != owner_id:
        return await msg.answer("У вас нет прав на удаление администратора.")
    
    await msg.answer("Введите ID администратора:")
    await AdminState.admin_id.set()

@dp.message_handler(state=AdminState.admin_id)
async def get_admin_id(msg: Message, state: FSMContext):
    admin_id = msg.text
    
    if admin_id.isdigit():
        admin_id = int(admin_id)
    else:
        await initiate_add_admin(msg)
    
    await state.update_data(admin_id=admin_id)
    await msg.answer("Введите имя администратора:")
    await AdminState.next()

@dp.message_handler(state=AdminState.admin_name)
async def get_admin_name(msg: Message, state: FSMContext):
    await state.update_data(admin_name=msg.text)
    await msg.answer("Введите контактную информацию администратора:")
    await AdminState.next()

@dp.message_handler(state=AdminState.admin_contact)
async def get_admin_contact(msg: Message, state: FSMContext):
    data = await state.get_data()
    db.add_admin(
        admin_id=data.get('admin_id'),
        admin_name=data.get('admin_name'),
        admin_contact=msg.text
    )

    await msg.answer("Администратор добавлен успешно!")
    await state.finish()
