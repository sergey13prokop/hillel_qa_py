# Напишите функцию func () так, чтобы она могла принимать аргументы переменной длины
# и выводить все значения аргументов с индексом аргумента.

def func(*args):
    for idx, arg in enumerate(args):
        print(f'Индекс {idx} : аргумент {arg}')


func(1, 22, 4, 0, 88)
