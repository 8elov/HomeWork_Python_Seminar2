# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def FindFactorial(num):
    fact_dict = []
    fact = 1
    for i in range(1, num + 1):
        fact *= i
        fact_dict.append(fact)
    print(*fact_dict, sep=', ')

n = int(input('Введите число: '))
FindFactorial(n)
