# Задача 0. Дан список, заполненный случайными числами от 0 до 10.
# Определите, является ли сумма всех элементов чётной.

import random
import string

length = 30
# numbers = [0] * length
# for index in range(length):
#     numbers[index] = random.randint(0, 10)
# print(numbers)

# numbers = [i for i in range(0, 10) if i % 2 == 0]
# print(numbers)

def generat(x):
    numbers = [random.randint(0, 25) for el in range(x)]
    print(numbers)
    return numbers
# sum = 0
# for index in range(length):
#     sum += numbers[index]
# print(f"Сумма всех элементов равна {sum}")
# if sum % 2 == 0:
#     print("Сумма чётная")
# else:
#     print("Сумма не чётная")


# Задача 1. В списке хранятся сведения о количестве осадков, выпавших за каждый день июня.
# Определите в какой период выпало больше осадков: в первой или второй половине июня.

def weather_in_june(x):
    num = generat(x)
    sum1 = 0
    sum2 = 0
    for i in range(15):
        sum1 += num[i]
    for i in range(15, 30):
        sum2 += num[i]
    if sum1 > sum2:
        print(f"Осадков больше выпало в первой половине: {sum1} - {sum2}")
    else:
        print(f"Осадков больше выпало во второй половине: {sum1} - {sum2}")


# Задача 2. Напишите программу, которая позволит пользователю заполнить анкету, последовательно вводя в программу:
# - имя;
# - возраст;
# - хобби;
# - любимое животное.
# После окончания ввода, выводится заполненная анкета.

def dict():
    dictionary = {}
    dictionary['name'] = input("Введите свое имя: ")
    dictionary['age'] = input("Введите свой возраст: ")
    dictionary['hobby'] = input("Введите свое хобби: ")
    dictionary['favorite_animal'] = input("Введите свое любимое животное: ")

    for (k, v) in dictionary.items():
        print(k + ":", v)


# Задача 3. Напишите скрипт генератора паролей заданной длины, состоящих из латинских букв и чисел.

def Task3(length):
    letters_and_digits = string.ascii_letters + string.digits
    password = ''.join(random.sample(letters_and_digits, length))
    print(password)

Task3(16)

# Задача 4. Ручка стоит – 5 рублей, карандаш – 3 рубля, ластик – 4 рубля.
# Кассир последовательно вводит в программу
# позиции из чека «ручка», «карандаш», «ластик».
# Ввод заканчивается, когда введено слово «стоп». Определите сумму чека.

def price():
    dict = {'Ручка':5, 'карандаш':3, 'ластик':4}
    sum = 0
    flag = True
    while flag:
        code = input('Введите наименование: ')
        if code in dict:
            sum += dict[code]
        elif code == 'стоп':
            flag = False          
    print(sum)