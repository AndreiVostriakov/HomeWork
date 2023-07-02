import random

# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию

def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)


# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

def num(arrey):
    for i in range(len(arrey)):
        if arrey[i] == max(arrey):
            arrey[i] = min(arrey)
    return arrey

# n = int(input("Введите кол-во оценок: "))
# list_1 = [random.randint(1, 5) for i in range(n)]
# print(list_1)

# list_2 = [1, 1, 1, 1, 1]

# print(*num(list_1))

# print(*num(list_2))


# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым.
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 

number = int(input('Input number: '))

def isSimple(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(isSimple(number))


# Задача №37.
# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

def reverse_sequence(n):
    if n == 0:
        return
    else:
        element = int(input())
        reverse_sequence(n - 1)
        print(element)