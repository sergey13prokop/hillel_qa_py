# Напишите программу для поэлементного вычисления суммы заданных кортежей.
# Результатом должен быть кортеж.
# Input
# (1, 2, 3, 4)
# (3, 5, 2, 1)
# (2, 2, 3, 1)
# Output
# (6, 9, 8, 6)

t1 = (1, 2, 3, 4, 17)
t2 = (3, 5, 2, 1)
t3 = (2, 2, 3, 1, 18, 91)
print("\nЗаданные кортежи:")
print(t1)
print(t2)
print(t3)

lTmp = list()

len_max = max(len(t1), len(t2), len(t3))
for i in range(0, len_max):
    itemTmp1 = 0 if i > len(t1)-1 else t1[i]
    itemTmp2 = 0 if i > len(t2)-1 else t2[i]
    itemTmp3 = 0 if i > len(t3)-1 else t3[i]
    lTmp.append(itemTmp1 + itemTmp2 + itemTmp3)
tOut = tuple(lTmp)

print("\33[34mСумма кортежей:")
print(tOut)