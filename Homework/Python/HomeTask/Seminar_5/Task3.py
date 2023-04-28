# Задача 3. Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего совпадающих элементов есть в списке. Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают. Список уникальных элементов

from random import randint

def create_list(size, m, n):
    return [randint(m, n) for i in range(size)]

def create_unic_list_value(list):
    return [i for i in set(list)]

# different = len(origin) - len()

size = int(input("Введите длину списка: "))
m = int(input("Введите минимальное значение для списка: "))
n = int(input("Введите максимальное значение для списка: "))

origin = create_list(size, m, n)
print(f"Исходный список - {origin}")
print(f"Список уникальных элементов {create_unic_list_value(origin)} => {len(origin) - len(create_unic_list_value(origin))} элементов(а) совпадают ")