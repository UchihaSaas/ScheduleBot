import requests
from bs4 import BeautifulSoup
groups_list = []
url = "https://elkaf.kubstu.ru/timetable/default/time-table-student-ofo"
responce = requests.get(url)
soup = BeautifulSoup(responce.text,'lxml')
all_groups = soup.find('select',id="nal_select_gr").find_all('option')
for group in all_groups:
    group = group.text
    groups_list.append(group)
print(groups_list)

