from random import randint

# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива

def task1():
    N_number = int(input("Введите кол-во элементов в первом массиве: "))
    M_number = int(input("Введите кол-во элементов во втором массиве: "))

    list_1 = [randint(0, 9) for i in range(N_number)]
    list_2 = [randint(0, 9) for i in range(M_number)]
    print(list_1)
    print(list_2)
    list_3 = []
    for i in list_1:
        if i not in list_2:
            list_3.append(i)
    print(*list_3)


# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел

def task2():
    N_number = int(input("Введите кол-во элементов в массиве: "))
    list_1 = [randint(0, 9) for i in range(N_number)]
    print(list_1)
    count = 0
    for i in range(1, len(list_1) - 1):
        if list_1[i - 1] < list_1[i] > list_1[i + 1]:
            count += 1
    print(f"Кол-во элементов = {count}")


# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках

def task3():
    N_number = int(input("Введите кол-во элементов в массиве: "))
    list_1 = [randint(0, 9) for i in range(N_number)]
    print(list_1)
    count = 0
    for i in range(len(list_1) - 1):
        for j in range(i + 1, len(list_1)):
            if list_1[i] == list_1[j]:
                count += 1
    print(f"Кол-во элементов = {count}")


# Задача №45. Решение в группах
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).

k_range = randint(10, 105)
for first_number in range(1, k_range):
    for second_number in range(first_number + 1, k_range):
        i = 1
        j = 1
        sum_div1 = 0
        sum_div2 = 0
        while i < first_number:
            if not first_number % i:
                sum_div1 += i
            i += 1
        while j < second_number:
            if not first_number % j:
                sum_div2 += j
            j += 1
        if sum_div1 == sum_div2 == sum_div1:
            print(f"Пара чисел {first_number} и {second_number} являются дружественными")


    # k_range = int(input('Введите диапозон '))
    # for first_number in range(1, k_range):
    #     for second_number in range(first_number + 1, k_range):
    #         i = 1
    #         j = 1
    #         sum_div1 = 0
    #         sum_div2 = 0
    #         while i < first_number:
    #             if first_number % i == 0:
    #                 sum_div1 += i
    #             i += 1
    #         while j < second_number:
    #             if second_number % j == 0:
    #                 sum_div2 += j
    #             j += 1

    #         if sum_div1 == second_number and sum_div2 == first_number:
    #             print(f"Пара чисел {first_number} и {second_number}")

    # input("Нажмите Enter что бы продолжить ")
    # system("cls")
