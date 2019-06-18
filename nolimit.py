"""Вечный генератор"""


def gen():
    """Функция-генератор"""
    list_1 = [1, 2, 3]
    for i in list_1:
        list_1.append(i)
        yield i


S = gen()

print(next(S))
print(next(S))
print(next(S))
print(next(S))
