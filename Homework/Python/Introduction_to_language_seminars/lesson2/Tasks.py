# Задача 0. Дано число N. Найти все его делители. Для каждого делителя укажите чётный он или нечётный.
# 	10 -> 10 (чётный), 5(нечётный), 2 (чётный), 1(нечётный)

def check(num):
    if num % 2 == 0:
        return "чётное"
    else:
        return "не чётное"


def zadacha():
    number = int(input("Введите число: "))

    for i in range(1, number + 1):
        if number % i == 0:
            print(f"{i} {check(i)}")


# Задача 1. Выведите таблицу истинности для выражения ¬ X ∨ Y.

def zadacha2():
    for X in range(0, 2):
        for Y in range(0, 2):
            print(f"{X} {Y} = {int(not(X) or Y)}")

# Задача 2. Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другую.

def zadacha3():
    substring = input("Введите текст №1: ")
    phrase = input("Введите текст №2: ")
    length_phrase = len(phrase)
    length_substring = len(substring)
    count = 0

    for i in range(length_phrase):
        if phrase[i:i + length_substring] == substring:
            count += 1
    print(f" в фразе \n{phrase} \подстрока {substring} встречается {count} раз(-а) ")


# Задача 3. Дано число N. Заполните список длиной N элементами 1, -3, 9, -27, 81, -243...
def zadacha4():
    N = int(input("Введите число: "))
    numbers = []
    for i in range(N):
        # print(f"{i} -> {(-3)**i}")
        numbers.append((-3)**i)
    print(numbers)
            

# Задача 4. Найдите все числа до 10000, у который количество делителей равно 10.

# def subtask5(num: int):
#     count = 0
#     for i in range(1, num+1):
#         if num % i == 0:
#             count += 1    
#     return count

# def task5():
#     for i in range(1,10001):
#         if subtask5(i) == 10:
#             print(f'{i}\t', end='')

def zadacha5():
    count = 0
    for num in range(1, 10001):
        count_div = 0
        for div in range(1, num + 1):
            if num % div == 0:
                count_div += 1
        if count_div == 10:
            count += 1
            print(num)
    print(f"Колличество чисел, у которых 10 делителей, равно {count}")
    
zadacha5()
