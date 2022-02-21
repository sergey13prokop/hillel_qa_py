# TASK 03
# Добавьте к исходному списку еще несколько товаров

list_orig = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]

list_add = [
    [24387, ' на русском', 2, 4.59],
    [18762, 'The C Programming Language (2nd Edition)', 12, 78.80],
    [87236, "C Programming Absolute Beginner's Guide", 1, 23.55],
    [58132, 'Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14', 9, 42.89]
]

list_orig.extend(list_add)
print("\n=== TASK 03 === Новый список с добавлением\33[34m")
for item in list_orig:
    print(item)

# TASK 04
# Отсортируйте получившийся список по стоимости и выведите его на экран.
# *Используйте lambda

list_orig.sort(key=lambda price: price[3])
print("\n\33[0m=== TASK 04 === Отсортированный новый список по стоимости\33[34m")
for item in list_orig:
    print(item)

# TASK 05
# Используя filter() оставьте только книги, количество которых больше 5ти.

print("\n\33[0m=== TASK 05 === Только книги, количество которых больше 5ти\33[34m")
for item in filter(lambda x: x[2] > 5, list_orig):
    print(item)

# Если необходимо фильтр применить в сам лист, то сначала делаем присвоение и код будет такой:
# list_orig = filter(lambda x: x[2] > 5, list_orig)
# for i in list_orig:
#     print(i)
