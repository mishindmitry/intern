"""Вечный генератор"""


def gen(i):
    """Функция-генератор"""
    while True:
        yield i


S = gen(3)

print(next(S))
print(next(S))
print(next(S))
print(next(S))
