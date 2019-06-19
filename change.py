"""Меняет местами ключ значение"""
A = {'a': 1, 'b': 2, 'qq': 3, 'c': 2, 'ss': 2, 'ssss': 2, 'qeqeq': 3}


def change(mydict):
    """Функция меняющая ключ-значение"""
    mydict_items = list(dict.items(mydict))
    mydict_new = {v: i for i, v in mydict_items}
    b_dict = mydict_new.copy()
    b_items = dict.items(b_dict)
    b_dict = {v: i for i, v in b_items}
    for i in mydict:
        if i not in b_dict:
            print('Ключ:', i, 'значение', mydict[i],
                  'не было добавлено(ДУБЛИКАТ КЛЮЧА)')
    return mydict_new


print(change(A))
