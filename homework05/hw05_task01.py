# Напишите функцию calculations () так,
# чтобы она могла принимать две переменные и вычислять их сложение и вычитание.
# А также он должен возвращать как сложение, так и вычитание за один вызов возврата.

def calculations(x, y):
    dictCalc = dict()
    dictCalc['сложение'] = x + y
    dictCalc['вычитание'] = x - y
    return dictCalc

x = int(input("\nВведите число x = "))
y = int(input("Введите число y = "))
print("\33[34mcalculations(x, y) =",calculations(x, y))