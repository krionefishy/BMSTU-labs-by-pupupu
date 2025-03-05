# Лабораторная работа 13
# Подготовил: Кошеваров Дмитрий 
# Назначение программы: реализация бд в текстовом файле

import os
import functions as functions 
import fake_data as fd
from colorama import *
import tkinter as tk
from PIL import Image, ImageTk
import time

def clean_console():
    os.system("cls")
    
    
def close_window():
    root.destroy()
    
def show_image():
    global root
    root = tk.Tk()
    root.title("show_image")
    root.attributes('-topmost', True)
    root.attributes("-fullscreen", True)
    image_path = "C:\\Users\\Kdima\\OneDrive\\Desktop\\pycourse\\lab13\\dropdbmeme.jpg"
    
    image = Image.open(image_path)
    image_tk = ImageTk.PhotoImage(image)
    
    label = tk.Label(root, image=image_tk)
    label.pack()

    label.image = image_tk
     
    root.after(5000, close_window)

    # Start the main application loop
    root.mainloop()
    
    
    
functions.menu()

n = input("Введите номер команды из меню: ")
current_file = ""
while n != "7":
    flag = False
    match n:
        case "1":
            filename = input("Введите название файла: ")
            p = functions.find_or_create_file(filename)
            print(Fore.CYAN + f"Путь к файлу: {p}")
            print(Fore.YELLOW + "Проверяем на валидность")
            err, output = functions.check_is_valid(p)
            if err == 0:
                print(output)
                current_file = p
            elif err == 1:
                print(output)
                current_file = p
            else:
                print(output)
        case "2":
            functions.extra_menu()
            command = input("Введите команду")
            flag = True
            while flag:
                match command:
                    case "1":
                        flag = False
                        n = int(input("Введите количество строк, которые вы хотите заполнить: "))
                        print("Введите данные в формате: \n \
                name;age;address;weight")
                        for i in range(n):
                            string = str(i) + ";" + input("Введите строку: ")
                            if len(string.split(";")) == 5:
                                functions.get_data_and_write(current_file, string)
                            else:
                                print("Данные не верны")
                    case "2":
                        flag = False
                        n = int(input("Введите количество строк, которые вы хотите заполнить: "))
                        fd.fill_with_fake_data(current_file, n)
                        print(Fore.GREEN + "Данные записаны")
                    case _:
                        command = input("Введите команду: ")
                        print(Fore.RED + "Такой команды нет, введите 1 или 2")
        case "3":
            functions.show_database(current_file)
        case "4":
            string = input("Введите строку в формате name;age;address;weight: ")
            if len(string.split(';')) == 4:
                functions.add_row(current_file, string)
            else:
                print("Введите строку по формату")
        case "5":
            n = float(input("Введите минимальный допустимый вес: "))
            if n <= 0:
                print("pupupu")
            else:
                functions.find_by_one(current_file, n)
            
        case "DROP TABLE":
            show_image()
            print("У тебя есть 5 секунд, чтобы убить работу программы и оставить DB жить")
            for i in range(5,0,-1):
                print(Fore.RED + str(i))
                time.sleep(1)
            print("Время вышло...")
            functions.drop_table(current_file)

        case "6":
            n = float(input("Введите минимальный допустимый вес: "))
            m = float(input("Введите минимальный допустимый возраст: "))
            if any(j <= 0 for j in [n,m]):
                print("pupupu")
            else:
                functions.find_by_two(current_file, n, m)
    
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
    
