"""Функция для получения входных данных от пользователя"""

from datetime import date
ALLOWED_DIRRECTION = {'CPH': 'Copenhagen', 'BLL': 'Billund', 'PDV': 'Plovdiv',
                      'BOJ': 'Burgas', 'SOF': 'Sofia', 'VAR': 'Varna'}
print('Обратите внимание на рассшифровку IATA-код\n')
for i in ALLOWED_DIRRECTION:
    print(i, '-', ALLOWED_DIRRECTION[i])


def start():
    """Функция для получения входных данных от пользователя"""
    while True:
        depart = input('\nВведите IATA-код откуда летим: ').upper()
        to = input('Введите IATA-код куда летим: ').upper()
        if depart not in ALLOWED_DIRRECTION or to not in ALLOWED_DIRRECTION:
            print('\nНеправильно введенн IATA-код.\nПовторите попытку.')
            continue
        today_date = date.today()
        try:
            date_from = input('Введите дату полёта формата(dd.mm.yyyy): ').split('.')
            date_from = date(int(date_from[2]), int(date_from[1]), int(date_from[0]))
            back = input('Введите дату обратного полета, если не летите, нажмите enter: ')
            if back:
                back = back.split('.')
                back = date(int(back[2]), int(back[1]), int(back[0]))
                if back < today_date:
                    raise Exception
                back = back.strftime('%d.%m.%Y')
            if date_from < today_date:
                raise Exception
            date_from = date_from.strftime('%d.%m.%Y')
        except Exception:
            print('Введена неверная дата')
            continue
        break
    return depart, to, date_from, back
