# Напишите программу Python для построения следующего шаблона, используя вложенный цикл for.
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

# В задании глубина шаблона = 5 (максимум звездочек на пике)
depth = int(input("\nВведите глубину шаблона: "))

print("\n\33[3mС ВЛОЖЕННЫМ ЦИКЛОМ")
for i in range(1, depth * 2):
    printStr = ""
    for _ in range(depth - abs(depth - i)):
        printStr += "*"
    print("\33[34m" + printStr)

print("\n\33[0m\33[3mБЕЗ ВЛОЖЕННОГО ЦИКЛА")
for i in range(1, depth * 2):
    print("\33[34m*"*(depth - abs(depth - i)))