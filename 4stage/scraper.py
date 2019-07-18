"""
Программа по считыванию rss файлов
с последующей закачкой торрент-файлов
"""
import re
from xml.etree import ElementTree
import shutil
from os.path import isfile, join
from os import listdir
import requests


RSS = 'Tokyo Toshokan.rss'
TREE = ElementTree.parse(RSS)
ROOT = TREE.getroot()

MYPATH = 'c:/python/fake/'
ONLYFILES = [f for f in listdir(MYPATH) if isfile(join(MYPATH, f))]

PROXIES = {
    'https': '51.158.108.135:8811',
}

LIST_CATEGORY = []
LIST_TITLE = []
LIST_LINK = []

for element in ROOT.iter('item'):
    result = re.sub(r'[\|\\/:*?><]', '', element.find('title').text)
    LIST_TITLE.append(result)
    LIST_LINK.append(element.find('link').text)
    if RSS == 'Nyaa.rss':
        LIST_CATEGORY.append(element.find(
            '{https://nyaa.si/xmlns/nyaa}category').text)
    else:
        LIST_CATEGORY.append(element.find('category').text)


NEED_CATEGORY = input('Вписать категорию если необходимо или нажмите enter')
FIND_ONE = input('Вписать ключевое слово если необходимо или нажмите enter')


MAIN_LIST = []
LIST_OF_LISTS = [LIST_CATEGORY, LIST_TITLE, LIST_LINK]
while all(LIST_OF_LISTS):
    MAIN_LIST.append(tuple(i.pop(0) for i in LIST_OF_LISTS))


def download(url, name):
    """Загрузка файла"""
    try:
        rec = requests.get(url, stream=True, proxies=PROXIES)
        with open('C:/python/fake/' + name + '.torrent', 'wb') as file:
            rec.raw.decode_content = True
            shutil.copyfileobj(rec.raw, file)
    except Exception as err:
        print(err)


if NEED_CATEGORY and FIND_ONE:
    for pack in MAIN_LIST:
        if FIND_ONE in pack[1] and NEED_CATEGORY in pack[0]:
            if pack[1] + '.torrent' in ONLYFILES:
                print('Уже есть')
            else:
                download(pack[2], pack[1])

elif NEED_CATEGORY:
    for pack in MAIN_LIST:
        if NEED_CATEGORY in pack[0]:
            if pack[1] + '.torrent' in ONLYFILES:
                print('Уже есть')
            else:
                download(pack[2], pack[1])

elif FIND_ONE:
    for pack in MAIN_LIST:
        if FIND_ONE in pack[1]:
            if pack[1] + '.torrent' in ONLYFILES:
                print('Уже есть')
            else:
                download(pack[2], pack[1])

else:
    for pack in MAIN_LIST:
        if pack[1] + '.torrent' in ONLYFILES:
            print('Уже есть')
        else:
            download(pack[2], pack[1])
