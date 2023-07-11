

# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
# *Пример:*
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
# **Вывод:** Парам пам-пам  

def task_1():
    text_1 = list(input('Введите текст песенки Винни-Пуха: ').split())
    print(text_1)
    list_1 = []
    quantity_of_vowel = 0
    vowel_letters = 'аеёиоуыэюя'
    for word in text_1:
        for letter in word:
            if letter in vowel_letters:
                quantity_of_vowel += 1
        list_1.append(quantity_of_vowel)
        quantity_of_vowel = 0
    if len(text_1) == list_1.count(list_1[0]):
        print('Парам пам-пам')
    else:
        print('Пам парам')


# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция,
# у которой ровно два аргумента, как, например, у операции умножения.
# *Пример:*
# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):
        numbers = []
        for j in range(1, num_columns + 1):
            numbers.append(operation(i, j))
        print(*numbers)

print_operation_table(lambda x, y: x * y)


# def print_operation_table_2(operation, num_rows=6, num_columns=6):
#     numbers = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
#     for i in numbers:
#         print(*[f'{j:2}' for j in i])

# print_operation_table_2(lambda x, y: x * y)


    
    




# list_3 = [[(i, j) for j in range(1, 6 + 1)] for i in range(1, 6 + 1)]
# print(list_3)