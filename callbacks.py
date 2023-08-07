from connect import bot,dp
import requests
from bs4 import BeautifulSoup
from aiogram import types
from handlers import ScheduleState
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from SupportDEF import get_day



@dp.callback_query_handler(state=ScheduleState.waitin_for_day)
async def process_schedule_message(call: types.CallbackQuery, state: FSMContext):
        data = await state.get_data()
        usergroup = data.get('group')
        schedule_message = call.data
        url = f"https://elkaf.kubstu.ru/timetable/default/time-table-student-ofo?iskiosk=0&fak_id=516&kurs=2&gr={usergroup}&ugod=2023&semestr=1"
        await get_day(data['chet_'],url,call,schedule_message)
        if schedule_message == "state.reset":
            await state.reset_state(with_data=False)


@dp.callback_query_handler(state=ScheduleState.waitin_for_week)
async def process_week_message(call: types.CallbackQuery, state: FSMContext):
    week_state = call.data
    await state.update_data(chet_=week_state)
    data = await state.get_data()
    await bot.send_message(call.from_user.id,f"Выбрана {data['chet_']} неделя,воспользуйтесь /рассписание")
    await state.reset_state(with_data=False)

@dp.callback_query_handler(state=ScheduleState.waitin_for_today)
async def process_today_message(call:types.CallbackQuery,state: FSMContext):
    data = await state.get_data()
    usergroup = data.get('group')
    today_week = data.get('week')
    today_chet = data.get('chet_')
    url = f"https://elkaf.kubstu.ru/timetable/default/time-table-student-ofo?iskiosk=0&fak_id=516&kurs=2&gr={usergroup}&ugod=2023&semestr=1"
    await get_day(today_chet,url,call,today_week)
    await state.reset_state(with_data=False)
