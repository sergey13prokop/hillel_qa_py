# Напишите функцию для умножения всех чисел в списке. Рекурсивно

import random

LIST_MAX_LEN = 4
ELEM_NUM_MIN = 1
ELEM_NUM_MAX = 10


def multi_list(lst, n=0):
    return 1 if n >= len(lst) else lst[n] * multi_list(lst, n + 1)


list_orig = [random.randint(ELEM_NUM_MIN, ELEM_NUM_MAX) for _ in range(0, random.randint(2, LIST_MAX_LEN))]
print(f'\nСписок: {list_orig}')
print(f'\33[34mПроизведение чисел: {multi_list(list_orig)}')
