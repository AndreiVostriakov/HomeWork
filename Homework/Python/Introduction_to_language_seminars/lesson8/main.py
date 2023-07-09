import os, shutil

# # massiv = [1, 2, 5, 10]
# # massiv = list(map(lambda x: str(x) + '\n', massiv))

# # with open('my_file.txt', 'w+') as f:
# #     f.writelines(massiv)

# os.getcwd()


# Задача №49. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

def read_file():
    with open('my_file.txt', 'r', encoding='utf-8') as f:
        for string in f:
            print(string)

def write_file():
    surname, name, phone = input("Введите Фамилию, Имя и телефон: ").split()
    with open('my_file.txt', 'a', encoding='utf-8') as f:
        f.writelines(f'\n{surname};')
        f.writelines(f'{name};')
        f.writelines(f'{phone}\n')


def serch_for_entry():
    pass

def menu():
    flag = True
    while flag:
        n = int(input('1 - поиск из справочника\n2 - запись в справочник\n3 - поиск\n0 - выход\n'))
        
        if n == 1:
            read_file()
        elif n == 2:
            write_file()
        elif n == 3:
            serch_for_entry() 
        elif n == 0:
            flag = False   
        else:
            print('Введите корректное значение')

if __name__ == '__main__':
    menu()




# import os
# from random import randint


# # Создать телефонный справочник с
# # возможностью импорта и экспорта данных в
# # формате .txt. Фамилия, имя, отчество, номер
# # телефона - данные, которые должны находиться
# # в файле.


# def read_file():
#     with open("phonebook.txt", "r", encoding="utf - 8") as f:
#         for string in f:
#             print(*string.strip().split(";"))


# def write_file():
#     with open("phonebook.txt", "a", encoding="utf - 8") as f:
#         new_phone = input("Введите новую запись ").replace(" ", ";") + "\n"
#         f.write(new_phone)


# def menu():
#     print(
#         "Нажмите 1 если хотите посмотреть справочник, Нажмите 2 если хотете внести запись или 3 что бы выйти из меню"
#     )
#     task_number = int(input("Укажите порядковый номер задачи, которую будем смотреть "))
#     if task_number == 1:
#         read_file()
#     elif task_number == 2:
#         write_file()

#     menu()


# if __name__ == "__main__":
#     menu()



# Код преподавателя

