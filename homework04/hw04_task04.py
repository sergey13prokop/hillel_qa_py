# Напишите программу, которая проверяет, присутствует ли А в наборе или нет.
# А вводится с клавиатуры

s = set(input("\nВведите строку для преобразования в множество: "))
A = input("Введите A: ")

isPresent = ('ВХОДИТ' if A in s else 'НЕ ВХОДИТ' )
print(f"\33[34m{A} {isPresent} в множество {s}")
