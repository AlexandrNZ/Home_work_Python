# 1. Открыть файл     
# 2. Сохранить файл
# 3. Показать тк      
# 4. Добавить контакт 
# 5. Найти контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход

import sys


# 1. Функция `open_file` открывает файл с телефонной книгой и возвращает его содержимое.
def open_file(file_name):
    with open(file_name, 'r') as f:
        phone_book = f.readlines()
    return phone_book


# 2. Функция `save_file` сохраняет изменения в телефонной книге в файл.
def save_file(file_name, phone_book):
    with open(file_name, 'w') as f:
        for contact in phone_book:
            f.write(contact)


# 3. Функция `show_phone_book` выводит на экран содержимое телефонной книги.
def show_phone_book(phone_book):
    for contact in phone_book:
        print(contact)


# 4. Функция `add_contact` добавляет новый контакт в телефонную книгу.
def add_contact(name, phone_number, phone_book):
    phone_book.append(name + ' - ' + phone_number + '\n')
    return phone_book


# 5. Функция `find_contact` находит контакт по имени и выводит его на экран.
def find_contact(name, phone_book):
    for contact in phone_book:
        if name in contact:
            print(contact)
            return contact
    print('Контакт не найден')
    return None


# 6. Функция `update_contact` изменяет информацию о контакте.
def update_contact(name, phone_number, phone_book):
    contact = find_contact(name, phone_book)
    if contact:
        index = phone_book.index(contact)
        phone_book[index] = name + ', ' + phone_number + '\n'
    return phone_book


# 7. Функция `delete_contact` удаляет контакт из телефонной книги.
def delete_contact(name, phone_book):
    contact = find_contact(name, phone_book)
    if contact:
        phone_book.remove(contact)
    return phone_book


# 8. Функция `exit` завершает программу.
def exit():
    sys.exit()


def phonebook_manager():
    file_name = 'phonebook.txt'
    phone_book = open_file(file_name)
    
    while True:
        action = input('Выберите действие:\n1 - Показать телефонную книгу\n2 - Добавить контакт\n3 - Найти контакт\n4 - Изменить контакт\n5 - Удалить контакт\n6 - Сохранить изменения\n7 - Выйти\n')
        
        if action == '1':
            show_phone_book(phone_book)
        elif action == '2':
            name = input('Введите имя: ').capitalize()
            phone_number = input('Введите номер телефона: ')
            phone_book = add_contact(name, phone_number, phone_book)
        elif action == '3':
            name = input('Введите имя: ')
            find_contact(name, phone_book)
        elif action == '4':
            name = input('Введите имя: ')
            phone_number = input('Введите новый номер телефона: ')
            phone_book = update_contact(name, phone_number, phone_book)
        elif action == '5':
            name = input('Введите имя: ')
            phone_book = delete_contact(name, phone_book)
        elif action == '6':
            save_file(file_name, phone_book)
            print('Изменения сохранены')
        elif action == '7':
            print('До свидания!')
            sys.exit()
        else:
            print('Некорректный ввод')
            
phonebook_manager()
            