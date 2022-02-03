# Напишите программу Python, которая принимает слово от пользователя и переворачивает его
# Пример: input - Hello Worlds output - sdlroW olleH

inputStr = input("\nВведите строку: ")
outputStr = ""

for i in range(len(inputStr), 0, -1):
    outputStr += inputStr[i - 1]

print("Зеркало строки: \33[34m\33[3m" + outputStr)