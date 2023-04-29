# Задача 2. Задан массив из случайных цифр на 15 элементов. На вход подаётся трёхзначное натуральное число.
# Напишите программу, которая определяет, есть в массиве последовательность из трёх элементов, совпадающая с введённым числом.
# [0, 5, 6, 2, 7, 7, 8, 1, 1, 9] - 277 -> да
# [4, 4, 3, 6, 7, 0, 8, 5, 1, 2] - 812 -> нет

from random import randint

def create_list():
    num = [randint(0, 9) for _ in range(15)]
    return num

def occurrence_of_number_elements(list_numbers, N):
    N = list(N)
    for i in range(len(N)):
        N[i] = int(N[i])
    for i in range(0, len(list_numbers) - 2):
        if list_numbers[i:i + 3] == N:
           return "Да"
    return "Нет"

list_numbers = create_list()
print(list_numbers)

N = input("Введите любое трёхзначное число: ")
if int(N) < 1000 and int(N) >= 100:
    print(occurrence_of_number_elements(list_numbers, N))
else:
    print("Число не является трёхзначным")
