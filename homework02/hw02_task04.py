# Определить високосный год или нет.
# Число вводится с клавиатуры

year = int(input("\nВведите год: "))

if (year % 4 != 0) or (year % 100 == 0 and year % 400 != 0):
    yearType = "НЕ ВИСОКОСНЫЙ"
else:
    yearType = "ВИСОКОСНЫЙ"

print("\n\033[34mГод {} {}".format(year, yearType))
