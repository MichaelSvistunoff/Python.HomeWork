"""Телефонный справочник
"""
from os import system
import os
import sys

# Добавить контакт
def add():
    clear_screen()
    print("Добавление нового контакта(для выхода нажмите Enter):\n")
    last_name = "empty"
    name = "empty"
    mid_name = "empty"
    number = "empty"
    while last_name and name and mid_name and number:
        last_name = input('Фамилия: ').title()
        if not last_name:
            break
        name = input('Имя: ').title()
        if not name:
            break
        mid_name = input('Отчество: ').title()
        if not mid_name:
            break
        number = input('Номер: ')
        if not number:
            break
        with open('phone-book.txt', 'a', encoding='utf8') as database:
            data = f"{last_name},{name},{mid_name},{number}\n"
            database.write(data)
        print(f"Добавлен(-а) '{name}' в контакты!\n")
    menu()

# Найти контакт по имени
def search_by_name():
    clear_screen()
    print("Поиск контакта по имени. Ввод с маленькой буквы (для выхода нажмите Enter):\n")
    input_ = "empty"
    while input_:
        input_ = input('Начните поиск: ').title()
        if not input_:
            break
        find = False
        with open('phone-book.txt', 'r', encoding='utf8') as database:
            lines = database.readlines()
            for line in lines:
                line = line.strip().split(",")
                if input_ in line[1]:
                    find = True
                    print(f"{line[0]},{line[1]},{line[2]},{line[3]}")
        if not find:
            print('Такой контакт не найден!')
        print()
    menu()

# Найти контакт по номеру
def search_by_phone():
    clear_screen()
    print("Поиск контакта по номеру:\n")
    input_ = "empty"
    while input_:
        input_ = input('Начните поиск: ').title()
        if not input_:
            break
        find = False
        with open('phone-book.txt', 'r', encoding='utf8') as database:
            lines = database.readlines()
            for line in lines:
                line = line.strip().split(",")
                if input_ in line[3]:
                    find = True
                    print(f"{line[0]},{line[1]},{line[2]},{line[3]}")
        if not find:
            print('Такой контакт не найден!')
        print()
    menu()

# Показать контакты
def show():
    clear_screen()
    with open('phone-book.txt', 'r', encoding='utf8') as database:
        lines = database.readlines()
        count = 0
        if lines:
            for line in lines:
                if line:
                    line = line.strip().split(",")
                    print(f"{line[0]},{line[1]},{line[2]},{line[3]}")
                    count += 1
            print(f"\nВ справочнике найдено {count} контактов")
        else:
            print('Пока нету контактов!')
    input('\nНажмите Enter, чтобы вернуться в меню')
    menu()

# Удалить контакт
def delete():
    clear_screen()
    print('Удаление контакта. Ввод с маленькой буквы (для выхода нажмите Enter):\n')
    name = "empty"
    while name:
        name = input('Введите фамилию контакта для удаления: ').title()
        if not name:
            break
        find = False
        with open('phone-book.txt', 'r', encoding='utf8') as database:
            lines = database.readlines()
            new_data = ''
            for line in lines:
                if name == line.strip().split(",")[0]:
                    find = True
                    print(f"Контакт '{name}' был удален")
                    continue
                new_data += line
        with open('phone-book.txt', 'w', encoding='utf8') as database:
            database.write(new_data)
        if not find:
            print(f"Контакт '{name}' не найден")
        print()
    menu()

# Изменить номер телефона
def edit_number():
    clear_screen()
    name = "empty"
    new_number = "empty"
    while name:
        name = input('Начните поиск для редактирования номера с маленькой буквы: ').title()
        if not name:
            break
        find = False
        with open('phone-book.txt', 'r', encoding='utf8') as database:
            lines = database.readlines()
            new_data = ''
            for line in lines:
                if name not in line:
                    new_data += line
                else:
                    find = True
                    line = line.strip().split(",")
                    print(f"{line[0]} -> {line[3]}")
                    new_number = input('Введите новый номер: ')
                    line[3] = new_number
                    line = f"{line[0]},{line[1]},{line[2]},{line[3]}\n"
                    print('Контакт успешно отредактирован!')
                    new_data += line
                    pass        
        with open('phone-book.txt', 'w', encoding='utf8') as database:
            database.writelines(new_data)                
        if not find:
            print("Такой контакт не найден!")
        print()
    menu()

# Выйти из приложения
def exit_():
    clear_screen()
    sys.exit()

# Очистить экран
def clear_screen():
    os.system("cls")

# Словарь меню
menu_dict = {
    "Показать все контакты": show,
    "Найти контакт по имени": search_by_name,
    "Найти контакт по номеру": search_by_phone,    
    "Добавить новый контакт": add,
    "Удалить контакт": delete,
    "Изменить номер телефона": edit_number,
    "Завершить программу": exit_,
}

# Пункты меню
menu_list = [
    "Показать все контакты",
    "Найти контакт по имени",
    "Найти контакт по номеру",
    "Добавить новый контакт",
    "Удалить контакт",
    "Изменить номер телефона",
    "Завершить программу",
]

# Телефонный справочник
def menu():
    clear_screen()
    print('Телефонный справочник\n')
    for index, option in enumerate(menu_list):
        print(f"{index+1} - {option}")
    input_ = input('Выбрать действие(введите индекс): ')
    while input_ not in ('1', '2', '3', '4', '5', '6', '7'):
        print('Пожалуйста, выберите 1, 2, 3, 4, 5, 6 или 7')
        input_ = input('Выберите действие(введите индекс): ')
    index_choose = int(input_[0])
    function = menu_dict[menu_list[index_choose-1]]
    function()

if __name__ == "__main__":
    try:
        with open('phone-book.txt', 'x'):
            pass
    except FileExistsError:
        pass

    menu()