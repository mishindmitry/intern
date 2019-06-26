"""Парсинг айпи"""
import re
k = 0
A = {}
with open('access2.log') as file:
    LINE = file.readlines()
    for i in LINE:
        try:
            k += 1
            g = re.search(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{0,3}', i)
            if g.group() in A:
                A[g.group()] += 1
            else:
                A[g.group()] = 1
        except AttributeError:
            print('В строке №', k, 'нет совпадений')

A_VAL = sorted(A.values())
A_VAL.reverse()
FINAL_LIST = []

if len(A_VAL) >= 9:
    for i in A_VAL[:10]:
        for k in A:
            if A[k] == i:
                if k not in FINAL_LIST:
                    FINAL_LIST.append(k)
else:
    for i in A_VAL:
        for k in A:
            if A[k] == i:
                if k not in FINAL_LIST:
                    FINAL_LIST.append(k)

for i in FINAL_LIST:
    print(i)
