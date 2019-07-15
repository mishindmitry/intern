"""Парсинг айпи"""
import re
import operator
from ua_parser import user_agent_parser
IP_AMOUNT = {}
k = 0
with open('access2.log') as file:
    LINE = file.readlines()
    for i in LINE:
        k += 1
        try:
            g = re.search(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{0,3}', i)
            if g.group() in IP_AMOUNT:
                IP_AMOUNT[g.group()] += 1
            else:
                IP_AMOUNT[g.group()] = 1
        except AttributeError:
            print('В строке №', k, 'нет совпадений')


SORTED_A = sorted(IP_AMOUNT.items(), key=operator.itemgetter(1))
for i in SORTED_A[-1:-11:-1]:
    print('ip:', i[0], 'кол-во посещений:', i[1])

"""Парсинг браузера"""

BROWSER_AMOUNT = {}
k = 0
with open('access2.log') as file:
    LINE = file.readlines()
    for i in LINE:
        k += 1
        try:
            ddd = user_agent_parser.ParseUserAgent(i)
            if ddd['family'] in BROWSER_AMOUNT:
                BROWSER_AMOUNT[ddd['family']] += 1
            else:
                BROWSER_AMOUNT[ddd['family']] = 1
        except Exception:
            print('В строке №', k, 'вызывается исключение')


SORTED_A = sorted(BROWSER_AMOUNT.items(), key=operator.itemgetter(1))
print('--------------------------------')
for i in SORTED_A[-1:-6:-1]:
    print('Browser:', i[0], 'кол-во посещений:', i[1])
