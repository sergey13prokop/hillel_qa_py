# Напишите программу, которая удаляет пересечение 2-го набора из 1-го набора.

set1 = set(input("\nВведите строку для преобразования в множество 1: "))
set2 = set(input("Введите строку для преобразования в множество 2: "))
print("\nМножество 1:", set1)
print("Множество 2:", set2)

set1.difference_update(set2)
print("\33[34mМножество 1 без пересечения с 2:", set1)