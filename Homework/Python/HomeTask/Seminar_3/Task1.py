# Задача 1. Создайте список. Запишите в него N первых элементов последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8

N = int(input("Введите число: "))
list_1 = [0] * N
if N == 1:
    list_1[0] = 1
elif N == 2:
    list_1[0] = 1
    list_1[1] = 1
else:
    list_1[0] = 1
    list_1[1] = 1
    for i in range(2, len(list_1)):
        list_1[i] = list_1[i - 2] + list_1[i - 1]
print(*list_1)