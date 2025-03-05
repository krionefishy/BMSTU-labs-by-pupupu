import os
from colorama import *

def menu():
    print(Fore.MAGENTA + "Выберите команду: \n \
    1) Выбор файла \n \
    2) Инициализировать БД \n \
    3) Вывести содержимое БД \n \
    4) Добавить запись  \n \
    5) Поиск по одному полю \n \
    6) Поиск по двум полям \n \
    7) ПУПУПУ \n \
    secret command: DROP TABLE")
    
def extra_menu():
    print(Fore.MAGENTA + "Выберите формат заполнения файла: \n\
    1) Заполнить файл самостоятельно \n\
    2) Заполнить файл рандомными данными \n")

def find_or_create_file(filename):
    default_path = "C:\\Users\\Kdima\\OneDrive\\Desktop\\pycourse\\lab13\\"
    if os.path.isabs(filename):
        file_path = filename
    else:
        file_path = os.path.join(default_path, filename)
    if os.path.exists(file_path):
        return file_path
    else:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("name;age;address;weight\n")
    return file_path
    
    
    
def check_is_valid(filename):
    exit_code = 0
    with open(filename, "r", encoding="utf-8") as f:
        topic = f.readline().strip("\n")
        if topic != "name;age;address;weight":
            exit_code = 2
            return exit_code, Fore.RED + "файл не валидный, выберите другой"
        
        
        first_string = f.readline().strip().strip("\n").split(";")
        while len(first_string) == 0:
            first_string = f.readline().strip().strip("\n").split(";")
            
        if len(''.join(first_string)) == 0:
            exit_code = 1
            return exit_code, Fore.GREEN + "файл пустой, можете выбрать команду 2 для заполнения"

        next_string = f.readline()
        if len(next_string) != 0 and ";" not in next_string:
            exit_code = 2
            return exit_code, Fore.GREEN + "файл не валидный, выберите другой"
        
        
        while next_string:
            next_string = next_string.strip().strip("\n").split(";")
            if len(next_string) == len(first_string) or len(next_string) == 0:
                next_string = f.readline()
            else:
                exit_code = 2
                return exit_code, "файл не валидный, выберите другой"
             
        else:
            exit_code = 0
            return exit_code, "файл валидный, можете продолжать"
            
            

def get_data_and_write(current_file, string):
    with open(current_file, "a", encoding="utf-8") as f:
        f.write(string + "\n")
        
    
def add_row(filename, string):
    with open(filename, "r", encoding = "utf-8") as f:
        s = len(f.readlines()) - 1
    with open(filename, "a+", encoding="utf-8") as f:
        f.seek(0,2)
        f.write(str(s) + ";" + string + "\n")
    
def show_database(current_file):
    with open(current_file, "r", encoding="utf-8") as f:
        string = f.readline().strip("\n")
        while string:
            idx,name,age,address,weight = string.split(";")
            print(f"{idx}:  \n \
        name: {name}; \n \
        age: {age}; \n \
        address: {address}; \n \
        weight: {weight}; \n ")
            string = f.readline().strip("\n")
      
def drop_table(filename):
     with open(filename, "w", encoding="utf-8") as f:
        f.seek(25,0)
        f.write("")   
        
        
def find_by_one(filename, minimum_weight):
    # weight 
    
    with open(filename, "r", encoding="utf-8") as f:
        s = f.readline().strip("\n").strip()
        s = f.readline().strip("\n").strip()
        while s:
            if float(s.split(";")[-1]) > minimum_weight:
                try:
                    idx,name,age,address,weight = s.split(";")
                    print(f"{idx}:  \n \
            name: {name}; \n \
            age: {age}; \n \
            address: {address}; \n \
            weight: {weight}; \n ")
                except:
                    ValueError
                    print(s)
            s = f.readline().strip().strip("\n")
            
            
            
def find_by_two(filename, minimun_weight, minimun_age):
    # weight 
    # age 
    with open(filename, "r", encoding="utf-8") as f:
        s = f.readline().strip("\n") .strip()
        s = f.readline().strip("\n").strip()
        while len(s) != 0:
            if float(s.split(";")[-1]) > minimun_weight and float(s.split(";")[2]) > minimun_age:
                idx,name,age,address,weight = s.split(";")
                print(f"{idx}:  \n \
        name: {name}; \n \
        age: {age}; \n \
        address: {address}; \n \
        weight: {weight}; \n ")
            s = f.readline().strip().strip("\n")
                
if __name__ == "__main__":
    pass