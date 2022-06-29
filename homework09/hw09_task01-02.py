# 1. Написать две функции которые выводят сумму первых 100 елементов последовательности Фибоначчи.
# Одна из функций должна использовать генератор
# 2. Задекорировать созданные функции так чтоб выводить время за которое эти функции выполняються
import time


def decortime(func):
    def func_arguments(arg1):
        timeStart = time.perf_counter()
        print("Сумма %s первых чисел Фибоначчи = %s, время выполнения %.10f" % (arg1, func(arg1), (time.perf_counter() - timeStart)))
    return func_arguments


@decortime
def fibosumm1(n):
    f1, f2, fSum = 0, 1, 0
    for _ in range(n):
        fSum += f1
        f1, f2 = f2, f1 + f2
    return fSum


@decortime
def fibosumm2(n):
    def fibonacci():
        fi1, fi2 = 0, 1
        while 1:
            yield fi1
            fi1, fi2 = fi2, fi1 + fi2

    gen = fibonacci()
    fiSum = 0
    for _ in range(n):
        fiSum += next(gen)
    return fiSum


n = int(input("\nВведите n = "))
fibosumm1(n)
fibosumm2(n)