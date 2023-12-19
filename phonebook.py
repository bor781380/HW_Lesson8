# Создать телефонный справочник с возможностью импорта и экспорта данных в # формате .txt. 
#Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
# записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной
# 5. Дополнить справочник возможностью копирования данных из одного файла в другой. 
# Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.

# Формат сдачи: ссылка на свой репозиторий.

def show_menu():
    print('1. Распечатать справочник ', sep = '\n')
    print('2. Найти телефон по фамилии ', sep = '\n')
    print('3. Изменить номер телефона ', sep = '\n')
    print('4. Удалить запись ', sep = '\n')
    print('5. Найти абонента по номеру телефона ', sep = '\n')
    print('6. Добавить абонента в справочник ', sep = '\n')
    print('7. Перенести запись в другой файл ', sep = '\n')
    print('8. Закончить работу', sep = '\n')
    choice = int(input("введите номер меню: "))
    return choice

def work_with_phonebook():
    choice=show_menu()
    phone_book=read_txt('phonebook.txt')
    
    while (choice!=8):
        if choice==1:
            print_txt(phone_book)
        elif choice == 2:
            last_name = input("Введите фамилию абонента: ")
            abonent = find_by_lastname(phone_book, last_name)
            if abonent:
                print_txt([abonent])
            else:
                print("\nАбонент не найден\n")
        elif choice==3:
            last_name=input("Введите фамилию абонента: ")
            new_number=input("Введите новый номер абонента: ")
            change_number(phone_book,last_name,new_number)            
            write_txt('phonebook.txt', phone_book)
        elif choice==4:
            last_name=input("Введите фамилию абонента: ")
            delete_by_lastname(phone_book,last_name)            
            write_txt('phonebook.txt', phone_book)
        elif choice == 5:
            number = input("Введите телефон абонента: ")
            abonent = find_by_number(phone_book, number)
            if abonent:
                print_txt([abonent])
            else:
                print("\nАбонент с таким номером отсутствует\n")
        elif choice==6:
            last_name=input("Введите фамилию абонента: ")
            first_name=input("Введите Имя абонента: ")
            number=input("Введите номер телефона абонента: ")
            description=input("Ведите описание абонента: ")
            add_user(phone_book,last_name,first_name, number, description)
            write_txt('phonebook.txt', phone_book)
        elif choice==7:
            print_line_txt(phone_book)
            line_number=input("Введите номер строки для копирования записи в файл: ")
            new_file=input("Введите имя файла в который скопировать запись: ")
            write_copy_line(new_file, phone_book, line_number)
        elif choice==8:
            break
        choice=show_menu()

def print_txt(filename):
    for item in filename:
        print('=' * 20)
        for key, value in item.items():
            print(f'{key}: {value.strip()}')
        print()

def find_by_lastname(phone_book, search_name):
    for item in phone_book:
        for i in item.values():
            if i == search_name:
                return dict(item)

def find_by_number(phone_book, search_number):
    for item in phone_book:
        for i in item.values():
            if search_number in i:
                return dict(item)
            
def change_number(phone_book, search_name, new_number):
    for item in phone_book:
        for key, value in item.items():
            if value == search_name:
                item['Телефон'] = new_number
                print('\nНомер абонента', search_name, 'изменен\n')
                return
    print('\nАбонент не найден\n')

def delete_by_lastname(phone_book,search_name):
    for item in phone_book:
        for key, value in item.items():
            if value == search_name:
                phone_book.remove(item)
                print('\nАбонент', search_name, 'удален из справочника\n')
                return
    print('\nАбонент не найден\n')

def add_user(phone_book,last_name,first_name, number, description):
    new_user = dict([('Фамилия', last_name), ('Имя', first_name), ('Телефон', number), ('Описание', description)])
    phone_book.append(new_user)
    print ('\nАбонент', last_name, 'с номером', number, 'добавлен в справочник\n')
    return()

def copy_account_user(phone_book, search_name, new_file):
    for item in phone_book:
        for key, value in item.items():
            if value == search_name:
                write_copy_txt(new_file, [item])
                print('\nАккаунт абонента', search_name, 'скопирован в файл', new_file, '\n')
                return
    print('\nАбонент не найден\n')
    
def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']     
    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            if line.strip() == '':
                continue
            record = dict(zip(fields,line.split(',')))
            phone_book.append(record)
    return phone_book

def write_txt(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s+=v+', '
            phout.write(f'{s[:-2]}\n')
                
def print_line_txt(phone_book):
    print(f'\n', '=' * 20)
    for line_number, line in enumerate(phone_book, start=1):
        print(f'{line_number}:', end=' ')
        print(', '.join(value.strip() for value in line.values()))
    print(f'\n', '=' * 20)

def write_copy_line(new_file, phone_book, line_number):
    line_number = int(line_number)
    if line_number <= len(phone_book):
        selected_line = phone_book[line_number - 1]
        with open(new_file, 'a', encoding='utf-8') as f:
            line_string = ', '.join(selected_line.values()) + '\n'
            f.write(line_string)
        print(f'\nЗапись скопирована в файл {new_file}\n')
    else:
        print('\nНедопустимый номер строки, операция не выполнена!\n')

work_with_phonebook()