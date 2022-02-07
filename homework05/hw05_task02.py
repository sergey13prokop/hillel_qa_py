# Напишите функцию Python для суммирования всех чисел в списке.

import random

LIST_MAX_LEN = 10
ELEM_NUM_MIN = -555
ELEM_NUM_MAX = 1000


def sum_list(lst):
    s = 0
    for i in range(0, len(lst)):
        s += lst[i]
    return s


list_orig = [random.randint(ELEM_NUM_MIN, ELEM_NUM_MAX) for _ in range(0, random.randint(1, LIST_MAX_LEN))]

print("\nСписок:", list_orig)
print("\33[34mСумма чисел:", sum_list(list_orig))
