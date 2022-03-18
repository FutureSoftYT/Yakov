from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode='HTML',disable_web_page_preview=True)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
