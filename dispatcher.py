from aiogram import Bot, Dispatcher
from config import API_TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token=API_TOKEN, parse_mode="HTML")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
