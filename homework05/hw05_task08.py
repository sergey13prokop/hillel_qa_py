# Дано натуральное число N.
# Выведите слово YES, если число N является точной степенью двойки,
# или слово NO в противном случае. 8 - YES, 3 - NO

def is_power_2(num):
    if num == 2:
        return 'YES'
    elif num % 2 == 1:
        return 'NO'
    else:
        return is_power_2(num // 2)


n = int(input("\nВведите натуральное n = "))
print(f'\33[34mТочная степень двойки: {is_power_2(n)}')
