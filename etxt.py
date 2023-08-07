from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

TOKEN_API = "6676667229:AAHB1rdYcQQgaFuHctSLCMzwup3VZ9_YoU4"
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/schedule')
kb.add(b1)
@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    await message.answer(reply_markup=kb)

if __name__ == '__main__':
    executor.start_polling(dp)