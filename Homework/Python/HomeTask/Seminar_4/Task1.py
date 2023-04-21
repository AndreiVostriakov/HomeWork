# Задача 1. Дано натуральное число N.
# Напишите метод, который вернёт список простых множителей числа N и количество этих множителей.

N = int(input("Введите натуральное число: "))

multiplay = []
count = 0
for i in range(2, 10):
    while N % i == 0:
        multiplay.append(i)
        count += 1
        N = N/i
print(*multiplay)
print(f"Кол-во множителей {count}")