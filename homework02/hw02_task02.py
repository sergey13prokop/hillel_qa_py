# Пользователь вводит трехзначное число.
# Найдите сумму его цифр. (используйте %)

number = int(input("\nВведите трёхзначное число: "))
if number < 100 or number > 999:
    print("\33[31mВы ввели не трёхзначное число")
else:
    firstNum = number // 100
    secondNum = number // 10 % 10
    thirdNum = number % 10
    print("\n\033[34mСумма цифр: ", firstNum + secondNum + thirdNum)