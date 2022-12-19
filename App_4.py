# 4. Реализуйте алгоритм перемешивания списка.
import random

def GetRAndomList(n):
    list = []
    for i in range(n):
        list.append(random.randint(0,100))
    return list  

n = int(input('Введите число элементов в списке: '))
list1 = GetRAndomList(n)
print('Прежний список:', list1)
list2 = random.sample(list1, n)
print('Новый список:', list2)