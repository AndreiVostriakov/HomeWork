from random import randint

# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Пример: ВВОД 7 2 5
# ВЫВОД 7 9 11 13 15

def task1():
    first_elemenr = int(input("Введите первый элемент арифметической прогрессии: "))
    difference = int(input("Введите разность: "))
    quantity_number = int(input("Введите кол-во элементов арифметической прогрессии: "))
    arithmetic_progression = []
    for i in range(0, quantity_number):
        arithmetic_progression.append(first_elemenr + i * difference)
        print(arithmetic_progression[i])
    print(arithmetic_progression)


# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Пример: ВВОД [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# ВЫВОД [1, 9, 13, 14, 19]

def task2():
    range_ot, range_do = int(input("Введите диапазон от: ")), int(input("Введите диапазон до: "))
    list_1 = [randint(0, 10) for i in range(20)]
    print(list_1)
    list_2 = []
    for i in range(len(list_1)):
        if list_1[i] >= range_ot and list_1[i] <= range_do:
            list_2.append(i)
    print(list_2)
    
