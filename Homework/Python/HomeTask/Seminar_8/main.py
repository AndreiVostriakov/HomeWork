def write_to_file(arg, do = 'a+'):
    if do == 'overwrite':
        symbol = "[]' "
        with open('phone_book.txt', 'w+', encoding='utf-8') as file:
            for i in arg:
                for j in symbol:
                    i = str(i).replace(j, '')
                file.writelines(f'{i}\n')
    else:
        surname, name, phone = arg()
        with open('phone_book.txt', do, encoding='utf-8') as file:
            file.writelines(f'{surname},')
            file.writelines(f'{name},')
            file.writelines(f'{phone}\n')

def name_subscriber():
    surname, name, phone = input("Введите Фамилию, Имя и телефон (через пробел): ").split()
    return surname, name, phone

def read_file():
    temp = []
    with open('phone_book.txt', 'r', encoding='utf-8') as file:
        for line in file:
            temp.append(line.replace('\n', '').split(','))
    return temp

def search_subscriber(arg_1, arg_2):
    for i in arg_1:
        for j in range(len(i)):
            if arg_2 == i[j]:
                return i
    return 0

def remove_subscriber(arg_1, arg_2, do = 'overwrite'):
    if arg_1 == 0:
        print('Такого абонента нет в справочнике')
    else:
        print(f'Будет удалён абонент:\n')
        beautiful_output_data(arg_1)
        arg_2.pop(arg_2.index(arg_1))
        print('Абонент удалён')
        write_to_file(arg_2, do)
                    
def change_subscriber(arg_1, arg_2, do = 'overwrite'):
    if arg_1 == 0:
        print('Такого абонента нет в справочнике')
    else:
        flag = True
        while flag:
            change_value = input('Что вы хотите изменить?\n1 - Фамилию\n2 - Имя\n3 - Телефон\n0 - выход в основное меню\n')
            if change_value == '1':
                new_value = input('Введите новое значение:\n')
                arg_1[0] = new_value
                write_to_file(arg_2, do)
            elif change_value == '2':
                new_value = input('Введите новое значение:\n')
                arg_1[1] = new_value
                write_to_file(arg_2, do)
            elif change_value == '3':
                new_value = input('Введите новое значение:\n')
                arg_1[2] = new_value
                write_to_file(arg_2, do)
            elif change_value == '0':
                flag = False
            else:
                print('Введите корректное значение')

def beautiful_output_data(arg):
    if arg == 0:
        print('Такого абонента нет в справочнике')
    else:
        print(f'Фамилия: {arg[0]}\nИмя: {arg[1]}\nНомер телефона: {arg[2]}\n')

def menu():
    flag = True
    while flag:
        data = read_file()
        n = input('\nМеню\n1 - показать весь справочник\n2 - записать в справочник\n3 - поиск по справочнику\n4 - изменить данные абонента\n5 - удалить абонента\n0 - выход из программы\n')
        if n == '1':
            for j in data:
                beautiful_output_data(j)
        elif n == '2':
            write_to_file(name_subscriber)
            print('Абонент успешно добавлен в справочник')
        elif n == '3':
            search_name = input('Введите любой 1 параметр для поиска (фамилия, имя, телефон):\n')
            beautiful_output_data(search_subscriber(data, search_name))
        elif n == '4':
            change_name = input('Введите любой 1 параметр для поиска (фамилия, имя, телефон):\n')
            change_subscriber(search_subscriber(data, change_name), data)
        elif n == '5':
            remove_name = input('Введите какого абонента необходимо удалить:\n')
            remove_subscriber(search_subscriber(data, remove_name), data)
        elif n == '0':
            flag = False
        else:
            print('Введите корректное значение')

if __name__ == '__main__':
    menu()


# Вводим в консоле

# Если нет, библиотеки. Установить
# pip install 

# для проверки какие библиотеки подключены
# # pip freeze

# Для создания виртуального окружения
# python -m venv venv
# souce venv/Scripts/activate

# Для записи имеющихся библиотек в файл
# pip freeze > requirements.txt

# Загрузки нужных библиотек чужого проекта
# pip install requirements.txt




# код преподавателя

# from tabulate import tabulate
# import csv


# def readfile(filename):
#     read_data = [i.strip().split(';') for i in open(filename, 'r', encoding='utf-8')]
#     # read_data = []
#     # with open('tel.txt', 'r', encoding='utf-8') as file:
#     #     for elem in file:
#     #         read_data.append(elem.split())
#     return read_data


# def menu():
#     print('===============================')
#     print('Выберите одно из действий:')
#     print('1 - вывести справочник на экран')
#     print('2 - произвести экпорт данных')
#     print('3 - поиск абонентов')
#     print('4 - удаление из справочника по id')
#     print('5 - добавление записи в справочник')
#     print('0 - выход из программы')

 
# def printinfo(data):
#     # print('id \t Фамилия Имя Отчество \t номер телефона')
#     # for elem in data:
#     #     print(*elem, sep='\t')
#     print(tabulate(data, headers=['id', 'ФИО', 'Телефон'], tablefmt='orgtbl'))

# def export_to_csv(data):
#     with open('example2.csv', 'w', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         writer.writerows(data)
#     print('Экспорт завершён')


# def search(data):
#     what = input('Что ищем? ')
#     searched_data = []
#     for string in data:
#         for elem in string:
#             if (what in elem) and string not in searched_data:
#                 searched_data.append(string)
#     if searched_data:
#         printinfo(searched_data)
#     else:
#         print('Строки, удовлетворяющие условиям поиска, не найдены')


# def delete(data):
#     id = input('Введите id для удаления: ')
#     new_data = []
#     for elem in data:
#         if elem[0] != id:
#             new_data.append(elem)
#     return new_data


# def add_record(data):
#     id = input('Введите id нового человека: ')
#     name = input('Введите ФИО нового человека: ')
#     tel = input('Введите номер телефона: ')
#     data.append((id, name, tel))
#     return data

# def save(data):
#     with open('tel.txt', 'w', encoding='utf-8') as file:
#         for elem in data:
#             stroka = ';'.join(elem) + '\n'
#             file.write(stroka)


# def main():
#     my_choice = -1
#     changed = False
#     # словарь номеров команд и привязанных к ним функций
#     operations = {
#         1: printinfo,
#         2: export_to_csv,
#         3: search,
#         4: delete,
#         5: add_record
#         }
#     data = readfile('tel.txt')
#     while my_choice != 0:
#         menu()
#         my_choice = int(input('Введите команду: '))
#         if 1 <= my_choice <= 3:
#             operations[my_choice](data)
#         elif 4 <= my_choice <= 5:
#             changed = True
#             data = operations[my_choice](data)
#         elif my_choice == 0:
#             if changed:
#                 print('Данные были изменены. Идёт сохранение данных')
#                 save(data)
#             print('До свидания')
#         else:
#             print('Введена неправильная команда')


# if __name__ == '__main__':
#     main()