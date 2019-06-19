"""Программа CAT"""
MAIN_DICT = {'i': 'я', 'am': 'есть', 'doctor': 'доктор', 'piano': 'пианино'}

print('Это программа CAT!!!')
print('Комбинация клавиш ctrl+с',
      'принудительно завершит программу'+'\n')
while True:
    with open('text_eng.txt', 'w') as file:
        file.write(input('Введите текст на английском: ').lower())

    with open('text_eng.txt') as file:
        for line in file:
            a = line.split()
    print(a, '\n')
    STOP = 0

    while STOP == 0:
        with open('text_rus.txt', 'w', encoding='utf-8') as file:
            try:
                for i in a:
                    file.write(MAIN_DICT[i]+' ')
            except KeyError:
                print('Найдено новое слово для словаря: ', '\'', i, '\'')
                MAIN_DICT[i] = input('Напишите перевод слова '+'\' ' +
                                     i+' \''+" :")
            else:
                STOP = 1

    with open('text_rus.txt', encoding='utf-8') as file:
        for line in file:
            print('ПЕРЕВОД:', line, '\n')
