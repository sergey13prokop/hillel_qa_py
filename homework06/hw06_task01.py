# сортировка пузырьком

def buble_sort(l):
    t = l.copy()
    for n in range(0, len(t)):
        # for i in range(len(t) - n):            # сравнение идет элемента со следующим, поэтому цикл нужен
        for i in range(len(t) - n - 1):          # без участия последнего в списке (части списка)
            # if t[i] > t[n]:
            #     t[i], t[n] = t[n], t[i]
            if t[i] > t[i + 1]:                  # сравниваться и меняться элемент должен всегда со следующим
                t[i], t[i + 1] = t[i + 1], t[i]
    return t


nums = [4, 1, 6, 3, 2, 7, 8]
print(f'\n{nums}\n\33[34m{buble_sort(nums)}\33[0m')

# Добавьте минимум 5 тестов для этого кода

nums = [0, 1, 2, 3, 4, 5, 0]
print(f'\n{nums}\n\33[34m{buble_sort(nums)}\33[0m')

nums = [0, 9, 8, -5, -5,]
print(f'\n{nums}\n\33[34m{buble_sort(nums)}\33[0m')

nums = [4]
print(f'\n{nums}\n\33[34m{buble_sort(nums)}\33[0m')

nums = []
print(f'\n{nums}\n\33[34m{buble_sort(nums)}\33[0m')

nums = [999999999999999, 8, 7, 6, 5, 4, -3]
print(f'\n{nums}\n\33[34m{buble_sort(nums)}\33[0m')

nums = [1, 2]
print(f'\n{nums}\n\33[34m{buble_sort(nums)}\33[0m')
