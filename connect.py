from aiogram import Bot,Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
TOKEN_API = "6676667229:AAHB1rdYcQQgaFuHctSLCMzwup3VZ9_YoU4"
bot = Bot(TOKEN_API)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
