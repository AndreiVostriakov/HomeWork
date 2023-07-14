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