# БЫСТРАЯ СОРТИРОВКА
# Два друга решили поиграть в игру: один загадывает число от 1 до 100, другой должен отгадать.

def quick_sort(array):
    if len(array) <= 1:
         return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]  # массив в которм все элементы меньше нашего числа
    greater = [i for i in array[1:] if i > pivot]  # массив в котором все элементы больше нашего числа
    return quick_sort(less) + [pivot] + quick_sort(greater)

# print(quick_sort([10, 5, 2]))


# СОРТИРОВКА СЛИЯНИЕМ
def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
            
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
            
# list_1 = [1, 5, 6, 9, 7, 2, 1, 55, 2, 4]
# merge_sort(list_1)
# print(list_1)


# Функция - это фрагмент программы, используемый многократно.

def sum_numbers(n, y = "Hello"):
    print(y)
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa

# a = sum_numbers(5, "qwerty")
# print(a)


def sum_str(*args):   # с помощью *args можно передавать неограниченное кол-во аргументов
    res = ""
    for i in args:
        res += str(i)
    return res

# print(sum_str(1, 8, 9))


def max1(a, b):
    if a > b:
        return a
    return b

# для импорта модуля из другого файла пишем 
# import имя_файла 
# from имя_файла import mmax1
# Eсли хотим импортировать все функции, то пишем from имя_файла import *
# Если хотим импортировать, с удобным именем для нас то пишем from имя_файла as новое_имя
# Для вывод в основном коде пишем print(имя_файла.max1(5, 9))

# print(max1(5, 9))


# Рекурсия - это функция которая вызывает сама себя
# При описани рекурсии важно указать, когда фенкции надо останавливаться и перестать вызывать саму себя.
# По-другому говоря, необходимо указать базис рекурсии

# Последовательность Фиббоначи
def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)

# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i))
# print(list_1)

# Алгоритмы

