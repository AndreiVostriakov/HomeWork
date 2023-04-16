# Создайте кортеж. Запишите в него 10 случайных чисел

import random

def kortage():
    numbers = tuple(random.randint(1 , 10) for _ in range(10))
    return numbers

def change_element(numbers, index):
    return numbers[:index] + (random.randint(1, 100), ) + numbers[index + 1:]
    

def calculate(n1, n2):
    return n1 + n2, n1 - n2, n1 * n2, n1 / n2


# num = kortage()
# index = 4

# print(num)
# num = change_element(num, index)
# print(num)



# def tupleAssign(tup, idx, value):
#     tup = tup[:idx] + (value,) + tup[idx + 1:]
#     return tup

# myTuple = tuple(randint(0, 9) for it in range(10))
# print(myTuple)
# myTuple = tupleAssign(myTuple, 2, "new")
# print(myTuple)


# numbers = tuple(random.randint(0,10) for _ in range(10))
# print(numbers)
# index = int(input('Выберете индекс: '))
# numbers = list(numbers)
# for i in range(len(numbers)):
#     if index == i:
#         numbers[i] = random.randint(0,10)
# numbers = tuple(numbers)
# print(numbers)


# Задача 2. На вход подаются два числа.
# Напишите метод, который вернёт сумму, разность, произведение и частное этих чисел.


def change_element(numbers, index):
    return numbers[:index] + (random.randint(1, 100), ) + numbers[index+1:]

def calculate(n1, n2):
    return n1 + n2, n1 - n2, n1 * n2, n1/ n2

def zadacha1():
    numbers = tuple(random.randint(1, 100) for _ in range(10))
    index = 2

    print(numbers)
    numbers_new = change_element(numbers, index)
    print(numbers_new)


def zadacha2():
    num_f = 9
    num_s = 3

    summ, raznost, umnozhenie, delenie = calculate(num_f, num_s)
    print(summ, raznost, umnozhenie, delenie)



# Сгенерируйте список случайных чисел от 1 до 20, состоящий из 10 элементов.
# Удалите из списка дубликаты уже имеющихся элементов.
# Определите, сколько элементов было удалено.

def zadacha3():
    numbers = list(random.randint(1,20) for _ in range(10))
    leng = len(numbers)
    print(numbers)
    numbers = set(numbers)
    leng2 = len(numbers)
    print(numbers)
    print(f'Удаленно элементов {leng - leng2}')
    


# Задача 4. Актёров разделили на списки по трём качествам «умные», «красивые», «сильные».
# На главную роль нужен актёр обладающий всеми тремя качествами.
# Определите, сколько есть претендентов на главную роль.
# Красивые: Илья Федор Семен Олег Лев Антон Артем Боря Стас Марк Ян
# Умные: Илья Георгий Лев Демьян Антон Владислав Боря Стас Марк Влад
# Сильные: Федор Георгий Олег Демьян Артем Елисей Боря Стас Влад

beuty = set("Илья Федор Семен Олег Лев Антон Артем Боря Стас Марк Ян".split())
clever = set("Илья Георгий Лев Демьян Антон Владислав Боря Стас Марк Влад".split())
strong = set("Федор Георгий Олег Демьян Артем Елисей Боря Стас Влад".split())

top = beuty.intersection(clever).intersection(strong)
print(top)