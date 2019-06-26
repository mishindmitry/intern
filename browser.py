"""Парсинг браузера"""
from ua_parser import user_agent_parser
A = {}
with open('access2.log') as file:
    LINE = file.readlines()
    for i in LINE:
        try:
            ddd = user_agent_parser.ParseUserAgent(i)
            if ddd['family'] in A:
                A[ddd['family']] += 1
            else:
                A[ddd['family']] = 1
        except:
            print('Ошибочка')


A_VAL = sorted(A.values())
A_VAL.reverse()
FINAL_LIST = []

for i in A_VAL[:5]:
    for k in A:
        if A[k] == i:
            if k not in FINAL_LIST:
                FINAL_LIST.append(k)

for i in FINAL_LIST:
    print(i, A[i])
