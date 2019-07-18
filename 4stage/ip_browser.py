
"""Парсинг айпи-браузер"""
import re
import operator
from ua_parser import user_agent_parser
IP_AMOUNT = {}
BROWSER_AMOUNT = {}
k = 0
PATH = input('Введите путь к файлу: ')
try:
    with open(PATH) as file:
        for line in file.readlines():
            ip = re.search(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{0,3}', line)
            if ip:
                ip = ip.group()
                IP_AMOUNT[ip] = IP_AMOUNT[ip]+1 if ip in IP_AMOUNT else 1
            browser = user_agent_parser.ParseUserAgent(line)
            family = browser['family']
            BROWSER_AMOUNT[family] = BROWSER_AMOUNT[family] + 1 if family in BROWSER_AMOUNT else 1
except Exception as err2:
    print(err2)


SORTED_A = sorted(IP_AMOUNT.items(), key=operator.itemgetter(1), reverse=True)
for i in SORTED_A[:10]:
    print('ip:', i[0], 'кол-во посещений:', i[1])


SORTED_A = sorted(BROWSER_AMOUNT.items(), key=operator.itemgetter(1), reverse=True)
print('--------------------------------')
for i in SORTED_A[:5]:
    print('Browser:', i[0], 'кол-во посещений:', i[1])
