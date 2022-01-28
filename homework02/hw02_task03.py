# Найти максимальное число из трех.
# Числа вводятся с клавиатуры

firstNum = int(input("\nВведите первое число: "))
secondNum = int(input("Введите второе число: "))
thirdNum = int(input("Введите третье число: "))

if firstNum > secondNum:
    maxNum = firstNum
else:
    maxNum = secondNum

if maxNum < thirdNum:
    maxNum = thirdNum

print("\n\033[34mМаксимальное число = ", maxNum)
