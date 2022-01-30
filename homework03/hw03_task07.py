# Напишите программу, которая копирует список.

import random

# символы A-Z это ASCII 65-90
DEC_FROM = 65
DEC_TO = 90
max_qty = int(input("\nВведите размерность списка: "))

listInt = [random.randint(DEC_FROM, DEC_TO) for _ in range(max_qty)] # генерим список ASCII кодов в нашем промежутке
listOrig = list(map(chr, listInt)) # пробегаемся по listInt функцией chr и получаем нужный список символов
print("\nИсходный список:\33[32m", listOrig)

# вариант 1
listNew = [elem for elem in listOrig]
print("\33[0mСкопированный-1:\33[34m",listNew)

listNew.clear()
# вариант 2
for i in range(0, len(listOrig)):
    listNew.append(listOrig[i])
print("\33[0mСкопированный-2:\33[35m",listNew)