# Реализовать логику Union для двух списков (list),
# проверить работу алгоритма на set.union

list1 = list(input("\nВведите строку для преобразования в список 1: "))
list2 = list(input("Введите строку для преобразования в список 2: "))

print("\nСписок 1:", list1)
print("Список 2:", list2)

list12 = list()
for i in range(0, len(list1)):
    list12.append(list1[i])
for i in range(0, len(list2)):
    list12.append(list2[i])

print("\n\33[34mВручную union:", list12)
print("\33[35mlist1 + list2:", list1 + list2)
print("\33[31mset.union:", set.union(set(list1), set(list2)))