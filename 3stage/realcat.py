"""CAT-программа"""
import sys

COUNT = 1
for i in sys.argv[2:]:
    try:
        with open(sys.argv[1] + i) as file:
            print('\nФАЙЛ ' + str(COUNT) + ':')
            COUNT += 1
            print(file.read())
    except FileNotFoundError:
        print('\nНет файла ' + i + ' или неправильный путь')
        COUNT += 1
