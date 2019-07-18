"""Программа для поиска полетов"""

import re
import operator
import sys
from decimal import Decimal
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
import start_data


def get_flight_data(arg1, arg2, arg3):
    """Делаем запрос, парсим таблицу с полетами.
    Всю информацию кидаем в общий пул"""
    try:
        url = 'https://apps.penguin.bg/fly/quote3.aspx?ow=&lang=en&depdate=' + arg1 +\
              '&aptcode1=' + arg2 + '&aptcode2=' + arg3 + '&paxcount=1&infcount='
        rec = requests.get(url)
        soup = BeautifulSoup(rec.text, 'html.parser')
        whole_flight_data_internal = []
        soup = soup.find('table', id="flywiz_tblQuotes").findAll('td')
    except Exception:
        print('Проблемы с подключением')
        sys.exit(1)
    for data in soup:
        if data.text:
            whole_flight_data_internal.append(data.text)
    return whole_flight_data_internal


def combine(data_list, any_date):
    """ Комплектует данные по каждому полету в список.
    Все комплекты упаковывает в общий список."""
    list_of_packs = []
    while data_list:
        pack_of_flight = []
        if len(data_list[0]) == 14:
            if data_list[0][5:7] == any_date[:2]:
                for _ in range(6):
                    pack_of_flight.append(data_list.pop(0))
                list_of_packs.append(pack_of_flight)
            else:
                data_list[0:6] = []
        else:
            if data_list[0][5] == any_date[1:2]:
                for _ in range(6):
                    pack_of_flight.append(data_list.pop(0))
                list_of_packs.append(pack_of_flight)
            else:
                data_list[0:6] = []
    for pack in list_of_packs:
        day = re.search(r'\d*\.\d{2}', pack[5])
        pack[5] = Decimal(day.group())
    list_of_packs.sort(key=operator.itemgetter(5))
    return list_of_packs


def result(list_1, place1, place2):
    """Краcивый вывод информации с учетом часовых поясов"""
    print('----Дата вылета: ' + list_1[0], '----Время вылета: ' +
          list_1[1], '----Время прибытия: ' + list_1[2], sep='\n')
    if place1 == 'CPH' or place1 == 'BLL' and place2 != 'CPH' or place2 != 'BLL':
        localisation = timedelta(hours=-1)
    elif place1 != 'CPH' or place1 != 'BLL' and place2 == 'CPH' or place2 == 'BLL':
        localisation = timedelta(hours=1)
    else:
        localisation = timedelta(hours=0)
    sformat = '%H:%M'
    time = datetime.strptime(list_1[2], sformat) - \
           datetime.strptime(list_1[1], sformat) + localisation
    print('----Время в полете: '+str(time)[:-3])
    print('----Стоимость:', str(list_1[5]) + ' EUR' + '\n')


DEPART, TO, DATE, BACK = start_data.start()

WHOLE_FLIGHT_DATA = get_flight_data(DATE, DEPART, TO)

LIST_OF_FLIGHT1 = combine(WHOLE_FLIGHT_DATA, DATE)

"""Если есть полет обратно"""
if BACK:
    WHOLE_FLIGHT_DATA = get_flight_data(BACK, TO, DEPART)
    LIST_OF_FLIGHT2 = combine(WHOLE_FLIGHT_DATA, BACK)

    """Собираем в пакет информацию о полете туда и обратно"""
    LIST_OF_FLIGHT3 = [[i, j] for i in LIST_OF_FLIGHT1 for j in LIST_OF_FLIGHT2]
    for i in LIST_OF_FLIGHT3:
        i.append(i[0][5]+i[1][5])

    # Отображение доступных полетов
    if not LIST_OF_FLIGHT3:
        if LIST_OF_FLIGHT1:
            print('\nДоступен только рейс в одну сторону до',
                  start_data.ALLOWED_DIRRECTION[TO])
            for i in LIST_OF_FLIGHT1:
                result(i, DEPART, TO)
        elif LIST_OF_FLIGHT2:
            print('\nДоступен только рейс в одну сторону до',
                  start_data.ALLOWED_DIRRECTION[DEPART])
            for i in LIST_OF_FLIGHT2:
                result(i, TO, DEPART)
        else:
            print('\nДоступных полетов на эти даты нет')
    else:
        LIST_OF_FLIGHT3.sort(key=operator.itemgetter(2))
        print('\nВозможные варианты полета: \n')
        COUNT = 1
        for i in LIST_OF_FLIGHT3:
            print('Вариант ' + str(COUNT) + ':')
            COUNT += 1
            print('--Полет туда:')
            result(i[0], DEPART, TO)
            print('--Полет обратно:')
            result(i[1], TO, DEPART)
            print('ОБЩАЯ СТОИМОСТЬ: ' + str(i[0][5] + i[1][5]) + ' EUR\n')
# Если полет обратно не был нужен
else:
    if LIST_OF_FLIGHT1:
        print('\n--Полет туда:')
        for i in LIST_OF_FLIGHT1:
            result(i, DEPART, TO)
    else:
        print('\nДоступных полетов на эту даты нет')
