# Дано натуральное число N. Вычислите сумму его цифр.
# Напишите рекурсивную функцию

def sum_digits(n):
    return n if n < 10 else sum_digits(n // 10) + n % 10


n = int(input("\nВведите натуральное число n = "))
print(f"\33[34mСумма цифр числа {n} равна {sum_digits(n)}")
