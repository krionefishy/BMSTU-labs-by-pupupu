# Лабораторная работа 14
# Подготовил Кошеваров Дмитрий
# Назначение программы: реализация базы данных в бинарном файле

import os
import functions
from colorama import *
import fill_with_fake_data as fd
import validators as v


def clean_console():
    os.system("cls")
functions.menu()

n = input("Введите номер команды из меню: ")
current_file = ""
while n != "8":
    flag = False
    match n:
        case "1":
            filename = input("Введите название файла: ")
            if v.filenameValidator(filename):
                p = functions.find_or_create_file(filename)
                print(Fore.CYAN + f"Путь к файлу: {p}")
                current_file = p
            else:
                print("Молодец, ставлю вам - 🤡, продолжайте в том же духе...")
        
        case "2":
            functions.extra_menu()
            command = input("Введите команду")
            flag = True
            while flag:
                match command:
                    case "1":
                        flag = False
                        n = input("Введите количество строк, которые вы хотите заполнить: ")
                        err, msg = functions.get_strings_from_user(current_file, n)
                        print(msg)
                        
                    case "2":
                        flag = False
                        n = input("Введите количество строк, которые вы хотите заполнить: ")
                        if v.intValidator(n):
                            n = int(n)
                            fd.fill_data(current_file, n)
                            print(Fore.GREEN + "Данные записаны")
                        else:
                            print("пупупу, на тебя очень осудительно смотрят 🤡")
                            
                    case _:
                        command = input("Введите команду: ")
                        print(Fore.RED + "Такой команды нет, введите 1 или 2")
        
        case "3":
            functions.show_table(current_file)
            
        case "4":
            string = input("Введите строку в формате name;age;weight: ")
            n = input("Введите номер строки, в которую надо записать данные: ")
            err, msg = functions.write_string(current_file, string, n)
            print(msg)
            
        case "5":
            n = input("Введите номер строки, которую надо удалить: ")
            err, msg = functions.delete_current_line(current_file, n)
            print(msg)
            
        case "6":
            n = input("Введите минимальный допустимый вес: ")
            functions.find_by_one_and_show(current_file, n)
            
        case "7":
            mw = input("Введите минимальный допустимый вес: ")
            ma = input("Введите минимальный допустимый возраст: ")
            functions.find_by_two_and_show(current_file, mw, ma)
            
        case _:
            n = input("Бу, испугался? Это я, разработчик,\n\
давай смотреть друг на друга, пока ты не введешь число из списка: ")
            flag = True
                
    functions.menu()
    if not flag: # докапываемся до пользователя, пока не введет норм команду
        n = input("Бу, испугался? Это я, разработчик,\n\
давай смотреть друг на друга, пока ты не введешь число из списка: ")

    clean_console()
else:
    print("(")   