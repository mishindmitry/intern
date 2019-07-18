"""Реализация ZIP"""
A = [1, 3, 4]
B = [2, 4]


def myzip(*seqs):
    """Функция реализующая ZIP"""
    seqs = [list(s) for s in seqs]
    res = []
    while all(seqs):
        res.append(tuple(s.pop(0) for s in seqs))
    return res


print(myzip(A, B))
