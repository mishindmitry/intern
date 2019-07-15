"""Меняет местами ключ значение"""


A = {'a': 1, 'b': 2, 'qq': 3, 'c': [1, 2, 3], 'ss': 2, 'ssss': 2, 'qeqeq': 3}


def change(mydict):
    """Функция меняющая ключ-значение"""
    mydict2 = {A[i]: i for i in A if not isinstance(A[i], (tuple, list, set))}
    difference = set(mydict2.values()) ^ set(mydict.keys())
    for i in difference:
        if isinstance(mydict[i], (tuple, list, set)):
            print('Ключ:', i, 'значение', mydict[i],
                  'не было добавлено(ИЗМЕНЯЕМЫЙ ОБЪЕКТ)')
        else:
            print('Ключ:', i, 'значение', mydict[i],
                  'не было добавлено(ДУБЛИКАТ КЛЮЧА)')
    return mydict2


print(change(A))
