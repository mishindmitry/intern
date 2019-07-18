"""Меняет местами ключ значение"""


A = {'a': 1, 'b': 2, 'qq': 3, 'c': [1, 2, 3], 'ss': 2, 'ssss': 2, 'qeqeq': 3}


def change(mydict):
    """Функция меняющая ключ-значение"""
    mydict2 = {}
    for i in mydict:
        try:
            if mydict[i] in mydict2:
                print('Ключ: ', mydict[i], 'значение', [i],
                      'не был добавлен(дубликат ключа)')
            else:
                mydict2[mydict[i]] = i
        except TypeError:
            print('Ключ: ', mydict[i], 'значение', [i],
                  'не был добавлен(изменяемый объект)')
    return mydict2


print(change(A))
