"""Реализация xrange"""


def my_xrange(start=0, stop=None, step=None):
    """Функция реализующая xrange"""
    res = []
    if step is None:
        if stop is None:
            counter = 0
            while counter != start:
                res.append(counter)
                yield counter
                counter += 1
        elif stop is not None:
            counter = start
            while counter != stop:
                res.append(counter)
                yield counter
                counter += 1
    else:
        counter = start
        while counter < stop:
            res.append(counter)
            yield counter
            counter += step


for i in my_xrange(10):
    print(i)

for i in my_xrange(0, 5):
    print(i)

for i in my_xrange(0, 10, 2):
    print(i)
