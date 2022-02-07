# Реализовать логику set.Union для двух списков (list),
# проверить работу алгоритма на set.union

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
    if list1[i] not in list12:
        list12.append(list1[i])
for i in range(0, len(list2)):
    if list2[i] not in list12:
        list12.append(list2[i])

print("\n\33[34munion.list:", list12)
print("\33[31mset.union :", set.union(set1, set2))