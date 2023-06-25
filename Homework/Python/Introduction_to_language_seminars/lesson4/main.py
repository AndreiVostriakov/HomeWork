from time import time
from sys import getsizeof

# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

def task0():
    start = time()
    # string_1 = "a a a b c a a d c d d".replace(" ", "")
    string_1 = "a a a b c a a d c d d".split()
    print(string_1)
    answer = ""
    # new_list = []
    # for elem in string_1:
    #     if elem in new_list:
    #         answer += elem + "_" + str(new_list.count(elem)) + " "
    #     else:
    #         answer += elem + " "
    #     new_list.append(elem)
    # print(answer)

def task1():
    string_1 = "a a a b c a a d c d d".split()
    my_dict = {}
    for elem in string_1:
        if elem in my_dict:
            answer += elem + "_" + str(my_dict[elem]) + " "
            my_dict[elem] += 1
        else:
            answer += elem + " "
            my_dict[elem] = 1
    print(answer)
    print(my_dict)

    finish = time()
    print(finish - start)
    print(getsizeof(my_dict))
    print(getsizeof(answer))


# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13


text_user = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells".upper().split()
set_1 = set(text_user)
print(len(set_1))

my_dict = {}
for elem in text_user:
    if elem in my_dict:
        my_dict[elem] += 1
    else:
        my_dict[elem] = 1
# print(my_dict)

for k,v in my_dict.items():
    if v == max(my_dict.values()):
        print ('{} встречается {} раз '.format(k, v))