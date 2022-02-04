# Напишите программу для преобразования списка в кортеж

import random
LIST_QTY = 10

l = [random.randint(0,9) for _ in range(0,LIST_QTY)]
print(f"\n{type(l)} : ", l)

t = tuple(l)
print(f"{type(t)}: \33[34m", t)