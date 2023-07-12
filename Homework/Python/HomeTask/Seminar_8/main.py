
def read_file():
    with open('phone_book.txt', 'r', encoding='utf-8') as f:
        for string in f:
            print(string)

def write_file():
    surname, name, phone = input("Введите Фамилию, Имя и телефон: ").split()
    with open('phone_book.txt', 'a', encoding='utf-8') as f:
        f.writelines(f'{surname};')
        f.writelines(f'{name};')
        f.writelines(f'{phone}\n')


def serch_for_entry():
    pass



def menu():
    data = read_file()
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
    
    
    
    
def read_file():
    with open('phone_book.txt', 'r', encoding='utf-8') as f:
        for string in f:
            print(string)
    

    
    
    
    
    
    
    
    
    
    
    
    
# def print_info(temp):
#     print(temp)


# def read_file():
#     with open('my_file.txt', 'r', encoding='utf-8') as file:
#         temp = file.readlines()
#     return temp

# def write_file():
#     pass

# def menu():
#     data = read_file()
#     while True:
#         print('Выберите действие: ')
#         print('1 - вывести инфо на экран')
#         print('0 - выход из программы')
#         n = int(input('ваш выбор: '))
#         if n == 0:
#             break
#         elif n == 1:
#             print_info(data)
#         # elif n == 3:
#         #     data = append(data)


# if __name__ == '__main__':
#     menu()