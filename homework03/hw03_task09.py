# Напишите программу для объединения следующих словарей для создания нового
# Исходные словари :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Результат : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic1 = dict([(1, 10), (2, 20)])
dic2 = dict([(3, 30), (4, 40)])
dic3 = dict([(5, 50), (6, 60)])

print("\nСловарь 1: ", dic1)
print("Словарь 2: ", dic2)
print("Словарь 3: ", dic3)

# вариант 1
dicUnion = dic1 | dic2 | dic3
print("\nUnion (1): \33[34m", dicUnion)

dicUnion.clear()
# вариант 2
for key in dic1:
    dicUnion[key] = dic1[key]
for key in dic2:
    dicUnion[key] = dic2[key]
for key in dic3:
    dicUnion[key] = dic3[key]
print("\33[0mUnion (2): \33[34m", dicUnion)