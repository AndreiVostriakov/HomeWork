import random

# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

def eagle_and_tail():
    quantity_coin = int(input("Введите кол-во монеток на столе: "))
    coin_on_table = []
    eagle = 0 # орёл это значение 1
    tail = 0 # решка это значение 0
    for i in range(quantity_coin):
        coin_on_table.append(random.randint(0, 1))

    print(coin_on_table)

    for j in coin_on_table:
        if j == 1:
            eagle += 1
        else:
            tail += 1

    if eagle > tail:
        print(f"Кол-во монет орлом вверх {eagle}. Необходимо перевернуть {tail} шт. той же стороной")
    elif eagle == tail:
        print(f"Кол-во монеток с орлом и решкой одинаково, и равно {eagle}. Выбирите какую из сторон монеты хотите видеть вверху и переверните {eagle} монеты")
    else:
        print(f"Кол-во монет решкой вверх {tail}. Необходимо перевернуть {eagle} шт. той же стороной")



# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

def mystery():
    number_1 = int(input("Загадайте первое число: "))
    number_2 = int(input("Загадайте второе число: "))
    sum_numbers = number_1 + number_2
    multiplication_numbers = number_1 * number_2
    print(f"Загадка. Сумма чисел равна {sum_numbers}. Произведение чисел равно {multiplication_numbers}. Какие это числа?")

    quantity_try = int(input("Введите кол-во попыток, за которое отгадаешь: "))
    while quantity_try != 0:
        first_number_kate = int(input("Первое число: "))
        second_number_kate = int(input("Второе число: "))
        if not multiplication_numbers % first_number_kate and not multiplication_numbers % second_number_kate and sum_numbers == first_number_kate + second_number_kate:
            print(f"Верно, это числа {first_number_kate} и {second_number_kate}. Молодец!")
            quantity_try = 0
        else:
            print(f"Не верно.")
            quantity_try -= 1
            if quantity_try > 0:
                print(f"Попробуй ещё. Кстати, у тебя осталось {quantity_try} попыток")
            else:
                print(f"Ты не разгадала загадку. Это числа {number_1} и {number_2}")
        
        

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

def exponentiation():
    num = int(input("Введите число: "))
    result = 0
    count = 0
    flag = True
    while flag:
        result = 2 ** count
        if result <= num:
            print(result)
            count += 1
        else:
            flag = False