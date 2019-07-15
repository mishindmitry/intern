"""3 функции"""


def square(seqs):
    """Функция возводит в квадрат каждый элемент списка"""
    return [i**2 for i in seqs]


def second(seqs):
    """Функция возвращает каждый четный элемент списка"""
    return [v for i, v in enumerate(seqs) if i % 2 != 0]


def square_odds(seqs):
    """Функция возводит в квадрат каждый четное число на нечетной позиции"""
    return [v**2 for i, v in enumerate(seqs) if i % 2 == 0 and v % 2 == 0]


print(square([1, 2, 3, 4, 5]))
print(second([1, 2, 3, 4, 5, 6]))
print(square_odds([4, 2, 2, 4, 5]))
