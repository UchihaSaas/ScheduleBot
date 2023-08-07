import requests
from bs4 import BeautifulSoup
from connect import bot,dp
def get_day(week,url_,call,schedule_message):

    response = requests.get(url_)
    days_dict = {
        "понедельник": 1,
        "вторник": 2,
        "среда": 3,
        "четверг": 4,
        "пятница": 5,
        "суббота": 6,
    }
    soup = BeautifulSoup(response.text, "lxml")
    weeks = soup.find_all('div', class_="col-md-6 ned-box")

    if week == 'нечетная':
        nedelya = weeks[0].find('div', class_='panel-info')
        day = nedelya.find('div', id=f'collapse_n_1_d_{days_dict.get(schedule_message)}')
    else:
        nedelya = weeks[1].find('div', class_='panel-info')
        day = nedelya.find('div', id=f'collapse_n_2_d_{days_dict.get(schedule_message)}')
    try:
        if day is not None:
            day_spans = day.find_all('span')
            schedule_text = ""
            count = 1
            for couple in day_spans:
                if week == 'нечетная':
                    panel = day.find('div', id=f'collapse_n_1_d_{days_dict.get(schedule_message)}_i_{count}').find('div', class_='panel-body').find_all('p')
                else:
                    panel = day.find('div', id=f'collapse_n_2_d_{days_dict.get(schedule_message)}_i_{count}').find(
                        'div', class_='panel-body').find_all('p')
                couple_text = couple.text
                schedule_text += couple_text + " " + f"{panel[1].text}" + "\n"
                count +=1
            return bot.send_message(call.from_user.id, schedule_text)
            return state.reset_state(with_data=False)
        if schedule_message == 'state.reset':
            return bot.send_message(call.from_user.id, "Вы отключили клавиатуру выбора для недели, чтобы ее вернуть введите /Schedule")
        else:
            return bot.send_message(call.from_user.id, "Нет пар на выбранный день")
    except Exception as e:
        return bot.send_message(call.from_user.id, f"Произошла ошибка: {e}")