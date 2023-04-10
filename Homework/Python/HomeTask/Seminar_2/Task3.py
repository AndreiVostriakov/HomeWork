# Задача 3.
# Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

word = input("Введите первую строку: ")
text = input("Введите вторую строку: ")

def occurrence_of_elements(line1, line2):
    length_word = len(line1)
    length_taxt = len(line2)
    count = 0

    for el in range(length_word):
        for i in range(length_taxt):
            if line1[el] == line2[i]:
                count += 1
        print(f"{line1[el]} встречается {count} раз(-а)")
        count = 0

occurrence_of_elements(word,text)

