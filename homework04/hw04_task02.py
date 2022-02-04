# Напишите программу для замены последнего значения кортежей в списке
# Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

NEW_VALUE = 99
listOrig = [(10, 20), (40, 50, 60, 30), (70, 80, 90)]
print("\nОригинальная строка: ", listOrig)

for i in range(0, len(listOrig)):
    listElem = list(listOrig[i])
    listElem[-1] = NEW_VALUE
    listOrig[i] = tuple(listElem)
print("Измененная строка  : \33[34m", listOrig)