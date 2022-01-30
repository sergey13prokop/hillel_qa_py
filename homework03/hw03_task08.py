# Напишите программу, которая находит разницу между двумя списками
# и сохраняет ее в новый список. Вывести результат на экран.

import random

NUM_FROM = 10
NUM_TO = 30
size_1 = int(input("\nВведите размерность списка 1: "))
size_2 = int(input("Введите размерность списка 1: "))

listOrig1 = [random.randint(NUM_FROM, NUM_TO) for _ in range(size_1)]
listOrig2 = [random.randint(NUM_FROM, NUM_TO) for _ in range(size_2)]
print("\nИсходный список 1:\33[32m", listOrig1)
print("\33[0mИсходный список 2:\33[32m", listOrig2)

listDiff = []
[listDiff.append(elem) for elem in listOrig1 if elem not in listOrig2]
[listDiff.append(elem) for elem in listOrig2 if elem not in listOrig1]
print("\33[0mРазница между списками:\33[34m", listDiff)