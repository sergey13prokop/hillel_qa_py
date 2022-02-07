# Реализовать логику Difference для двух списков (list),
# проверить работу алгоритма на set.difference

list1 = list(input("\nВведите строку для преобразования в список и множество 1: "))
list2 = list(input("Введите строку для преобразования в список и множество 2: "))
set1 = set(list1)
set2 = set(list2)

print("\nСписок 1:", list1)
print("Список 2:", list2)
print("\nМножество 1:", set1)
print("Множество 2:", set2)

list12 = list()
for i in range(0, len(list1)):
    if list1[i] not in (list12 + list2):
        list12.append(list1[i])

print("\n\33[34mlist1.difference(list2):", list12)
print("\33[31m set1.difference(set2) :", set1.difference(set2))