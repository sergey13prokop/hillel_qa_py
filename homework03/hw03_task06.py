# Напишите программу, которая удаляет дубликаты элементов из списка.

import random

# символы A-Z это ASCII 65-90,
# используем какой-то небольшой промежуток, чтобы были совпадения
DEC_FROM = 65
DEC_TO = 72
max_qty = int(input("\nВведите размерность списка: "))

listInt = [random.randint(DEC_FROM, DEC_TO) for _ in range(max_qty)] # генерим список ASCII кодов в нашем промежутке
listOrig = list(map(chr, listInt)) # пробегаемся по listInt функцией chr и получаем нужный список символов
print("\nИсходный список:\33[32m", listOrig)

listNew = []
for elem in listOrig:
    if elem not in listNew:
        listNew.append(elem)
print("\33[0mБез дубликатов :\33[34m",listNew)
