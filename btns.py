from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton,ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove

ink = InlineKeyboardMarkup()
bnt1 = InlineKeyboardButton(text='понедельник', callback_data='понедельник')
bnt2 = InlineKeyboardButton(text='вторник', callback_data='вторник')
bnt3 = InlineKeyboardButton(text='среда', callback_data='среда')
bnt4 = InlineKeyboardButton(text='четверг', callback_data='четверг')
bnt5 = InlineKeyboardButton(text='пятница', callback_data='пятница')
bnt6 = InlineKeyboardButton(text='суббота', callback_data='суббота')
bnt7 = InlineKeyboardButton(text='cancel', callback_data='state.reset')
ink.add(bnt1, bnt2, bnt3, bnt4, bnt5, bnt6,bnt7)

ink_odd = InlineKeyboardMarkup()
chet = InlineKeyboardButton(text= 'четная', callback_data='четная')
nechet = InlineKeyboardButton(text= 'нечетная', callback_data='нечетная')
ink_odd.add(chet,nechet)

ink_today = InlineKeyboardMarkup()
get_shit = InlineKeyboardButton(text= 'получить рассписание' ,callback_data='A v been on det drugs')
ink_today.add(get_shit)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(KeyboardButton('/расписание'))
kb.add(KeyboardButton('/выключить'))
kb.add(KeyboardButton('/сегодня'))
kb.add(KeyboardButton('/информация'))
kb.add(KeyboardButton('/группа'))
kb.add(KeyboardButton('/неделя'))

