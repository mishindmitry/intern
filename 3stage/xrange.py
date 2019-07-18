"""Реализация xrange"""


def my_xrange(start=0, stop=None, step=1):
    """Реализация xrange"""
    if stop is None:
        start, stop = 0, start
    while start > stop if step < 0 else start < stop:
        yield start
        start += step


for k in my_xrange(10):
    print(k, end=' ')
print('\n')

for k in my_xrange(0, 5):
    print(k, end=' ')
print('\n')

for k in my_xrange(10, 0, -1):
    print(k, end=' ')
