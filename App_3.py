# Задайте список из n чисел последовательности (1 + 1/n) ** n и выведите на экран их сумму.
# Пример:
# -Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
# Сумма 9.06

def GetListAndSum(num):
    out_dict = {}
    summ = 0
    for i in range(1, n + 1):
        out_dict[i] = round((1 + (1 / i)) ** i, 2)
        summ += out_dict[i]
    print(out_dict)
    print('Сумма', summ)

n = int(input('Введите число: '))
GetListAndSum(n)