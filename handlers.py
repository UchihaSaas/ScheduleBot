import requests
from bs4 import BeautifulSoup
from connect import bot,dp
from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup
from btns import kb,ink,ink_odd,ink_today
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from grouplist import groups_list

class ScheduleState(StatesGroup):
    waitin_for_day = State()
    waitin_for_group = State()
    waitin_for_week = State()
    waitin_for_today = State()


@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    await bot.send_message(text= 'Whats up🫡',chat_id=message.from_user.id, reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['выключить'])
async def cancel_bot(message:types.Message):
     await bot.send_message(text= 'Клавиатура отключена😴',chat_id=message.from_user.id,reply_markup=ReplyKeyboardRemove())
     await message.delete()


@dp.message_handler(commands=['сегодня'])
async def get_today(message:types.Message,state: FSMContext):
    data = await state.get_data()
    usergroup = data.get('group')
    if usergroup:
        url = "https://elkaf.kubstu.ru/timetable/default/time-table-student-ofo?iskiosk=0&fak_id=516&kurs=2&gr=22-%D0%9A-%D0%9A%D0%911&ugod=2023&semestr=1"
        responce = requests.get(url)
        soup = BeautifulSoup(responce.text,'lxml')
        today = soup.find('p',style = 'font-style: normal;').text
        p = today.split(";")
        await message.answer(today,reply_markup=ink_today)
        chet_today = p[2].split(' ')[-1]
        week_today = p[3].split(' ')[-1].lower()
        await state.update_data(chet_ = chet_today)
        await state.update_data(week =week_today)
        await message.delete()
        await ScheduleState.waitin_for_today.set()
    else:
        await message.answer('Укажите номер группы')


@dp.message_handler(commands=['расписание'])
async def cmd_schedule(message: types.Message, state: FSMContext):
    data = await state.get_data()
    usergroup = data.get('group')
    if usergroup:
        await message.answer(f"Номер вашей группы: 🥶<b>{usergroup}</b>🥶 .Вы выбрали👉 <u> {data['week_odd']} </u>👈неделю Пожалуйста, введите день недели:",reply_markup=ink,parse_mode='HTML')
        await ScheduleState.waitin_for_day.set()
        await message.delete()
    else:
        await message.answer(r"Группа не указана🛑. Введите /группа для установки группы.")
        await message.delete()


@dp.message_handler(state=ScheduleState.waitin_for_group)
async def set_group(message: types.Message, state: FSMContext):
    if message.text not in groups_list:
        await message.reply('Такой группы нет😔, введите верный номер группы')
    else:
        await state.update_data(group=message.text)
        await state.reset_state(with_data=False)
        await message.answer("Номер группы сохранен✅. Чтобы ввести четность недели воспользуйтесь командой /неделя")

@dp.message_handler(commands=['группа'])
async def cmd_group(message: types.Message, state: FSMContext):
    await message.answer("Введите свою группу:")
    await ScheduleState.waitin_for_group.set()
    await message.delete()
@dp.message_handler(commands=['неделя'])
async def week_parity(message: types.Message,state:FSMContext):
    await message.answer("Укажите четность недели",reply_markup=ink_odd)
    await ScheduleState.waitin_for_week.set()
    await message.delete()


@dp.message_handler(commands=['информация'])
async def cmd_info(message: types.Message, state: FSMContext):
    info_text = """
    Для старта бота введите /start
    Для получения расписания введите /рассписание
    Для отключения вспомогательной клавиатуры введите /выключить
    Для изменения или установки статуса группы введите /группа
    Для изменения или установки статуса четности недели введите /неделя
    Для того чтобы узнать какой сегодня день введите /сегодня
    """
    await message.answer(info_text)
    await message.delete()