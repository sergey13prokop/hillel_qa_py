# Определить четное или нечетное число.
# Число вводится с клавиатуры

number = int(input("\nВведите число: "))

print("\n\033[34mЭто число", "ЧЕТНОЕ" if number % 2 == 0 else "НЕЧЕТНОЕ")