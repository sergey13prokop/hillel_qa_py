# Напишите рекурсивную функцию для вычисления числа Фибоначи

def fibonachi(n):  # считаем ряд, начиная с нуля: 0,1,1,2...
    return n - 1 if n < 3 else fibonachi(n - 2) + fibonachi(n - 1)


n = int(input("\nВведите порядковый номер числа Фибоначчи n = "))
print(f"\33[34mЧисло Фибоначчи номер {n} равно {fibonachi(n)}")