"""Программа для поиска полетов"""

import re
import operator
import sys
from decimal import Decimal
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup


ALLOWED_DIRRECTION = {'CPH': 'Copenhagen', 'BLL': 'Billund', 'PDV': 'Plovdiv',
                      'BOJ': 'Burgas', 'SOF': 'Sofia', 'VAR': 'Varna'}
print('Обратите внимание на рассшифровку IATA-код\n')
for i in ALLOWED_DIRRECTION:
    print(i, '-', ALLOWED_DIRRECTION[i])

"""Получение данных от пользователя"""
while True:
    DEPART = (input('\nВведите IATA-код откуда летим: '))
    DEPART = DEPART.upper()
    TO = (input('Введите IATA-код куда летим: '))
    TO = TO.upper()
    try:
        DATE = (input('Введите дату полёта формата(dd.mm.yyyy): '))
        B = re.match(r'([0-3]((?<=[3])[0-1]||(?<=[0-2])[0-9]))\.' +
                     r'([0-1]((?<=[0])[0-9]||(?<=[1])[0-2]||))\.[0-9]{4}', DATE)
        B.group()
        BACK = (input('Введите дату обратного полета, если не летите, нажмите enter: '))
        if BACK:
            B = re.match(r'([0-3]((?<=[3])[0-1]||(?<=[0-2])[0-9]))\.' +
                         r'([0-1]((?<=[0])[0-9]||(?<=[1])[0-2]||))\.[0-9]{4}', BACK)
            B.group()
    except AttributeError:
        print('Введена неверная дата')
        continue
    if DEPART in ALLOWED_DIRRECTION and TO in ALLOWED_DIRRECTION:
        break
    print('\nНеправильно введенн IATA-код.\nПовторите попытку.')


def get_flight_data(any_url):
    """Делаем запрос, парсим таблицу с полетами.
    Всю информацию кидаем в общий пул"""
    try:
        rec = requests.get(any_url)
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


def combine(spis_from, spis_to, any_date):
    """ Комплектует данные по каждому полету в список. Все комплекты упаковывает в общий список."""
    while spis_from:
        pack_of_flight = []
        if len(spis_from[0]) == 14:
            if spis_from[0][5:7] == any_date[:2]:
                for _ in range(6):
                    pack_of_flight.append(spis_from.pop(0))
                spis_to.append(pack_of_flight)
            else:
                spis_from[0:6] = []
        else:
            if spis_from[0][5] == any_date[1:2]:
                for _ in range(6):
                    pack_of_flight.append(spis_from.pop(0))
                spis_to.append(pack_of_flight)
            else:
                spis_from[0:6] = []


def result(list_1, place1, place2):
    """Краивый вывод информации с учетом часовых поясов"""
    print('----Дата вылета: ' + list_1[0], '----Время вылета: ' +
          list_1[1] + ':00', '----Время прибытия: ' + list_1[2] + ':00', sep='\n')
    if place1 == 'CPH' or place1 == 'BLL' and place2 != 'CPH' or place2 != 'BLL':
        sformat = '%H:%M'
        time = datetime.strptime(list_1[2], sformat) - \
               datetime.strptime(list_1[1], sformat) - timedelta(hours=1)
        print('----Время полета: '+str(time))
    elif place1 != 'CPH' or place1 != 'BLL' and place2 == 'CPH' or place2 == 'BLL':
        sformat = '%H:%M'
        time = datetime.strptime(list_1[2], sformat) - \
        datetime.strptime(list_1[1], sformat) + timedelta(hours=1)
        print('----Время полета: ' + str(time))
    else:
        sformat = '%H:%M'
        time = datetime.strptime(list_1[2], sformat) - datetime.strptime(list_1[1], sformat)
        print('----Время полета: ' + str(time))
    print('----Стоимость: ', str(list_1[5]) + ' EUR' + '\n')


URL = 'https://apps.penguin.bg/fly/quote3.aspx?ow=&lang=en&depdate=' + DATE +\
'&aptcode1=' + DEPART + '&aptcode2=' + TO + '&paxcount=1&infcount='

WHOLE_FLIGHT_DATA = get_flight_data(URL)
LIST_OF_FLIGHT1 = []
combine(WHOLE_FLIGHT_DATA, LIST_OF_FLIGHT1, DATE)

"""Поиск цифр в строке с ценой с последующим преобразованием в decimal для сортировки по цене"""
for i in LIST_OF_FLIGHT1:
    a = re.search(r'\d*\.\d{2}', i[5])
    i[5] = Decimal(a.group())

LIST_OF_FLIGHT1.sort(key=operator.itemgetter(5))

"""Если есть полет обратно"""
if BACK:
    URL = 'https://apps.penguin.bg/fly/quote3.aspx?ow=&lang=en&depdate=' + BACK + \
    '&aptcode1=' + TO + '&aptcode2=' + DEPART + '&paxcount=1&infcount='

    WHOLE_FLIGHT_DATA = get_flight_data(URL)

    LIST_OF_FLIGHT2 = []
    combine(WHOLE_FLIGHT_DATA, LIST_OF_FLIGHT2, BACK)

    """Поиск цифр в строке с ценой
    с последующим преобразованием в decimal для сортировки по цене"""
    for i in LIST_OF_FLIGHT2:
        a = re.search(r'\d*\.\d{2}', i[5])
        i[5] = Decimal(a.group())

    """Собираем в пакет информацию о полете туда и обратно"""
    LIST_OF_FLIGHT3 = [[i, j] for i in LIST_OF_FLIGHT1 for j in LIST_OF_FLIGHT2]
    for i in LIST_OF_FLIGHT3:
        i.append(i[0][5]+i[1][5])

    # Отображение доступных полетов
    if not LIST_OF_FLIGHT3:
        if LIST_OF_FLIGHT1:
            print('Доступен только рейс в одну сторону до', ALLOWED_DIRRECTION[TO])
            for i in LIST_OF_FLIGHT1:
                result(i, DEPART, TO)
        elif LIST_OF_FLIGHT2:
            print('Доступен только рейс в одну сторону до', ALLOWED_DIRRECTION[DEPART])
            for i in LIST_OF_FLIGHT2:
                result(i, TO, DEPART)
        else:
            print('Доступных полетов на эти даты нет')
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
        print('Доступных полетов на эти даты нет')
