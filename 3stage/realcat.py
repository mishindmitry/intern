"""CAT-программа"""
import sys

FILES = sys.argv[1:]
if not FILES:
    print('Укажите путь к файлу')


for path in FILES:
    try:
        with open(path) as file:
            print(file.read())
    except FileNotFoundError:
        print('Такого файла нет')
