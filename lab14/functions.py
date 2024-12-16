from colorama import *
import struct
import os 
import validators as v


def menu():
    print(Fore.MAGENTA + "Выберите команду: \n \
    1) Выбор файла \n \
    2) Инициализировать БД \n \
    3) Вывести содержимое БД \n \
    4) Добавить запись \n \
    5) Удалить поле \n \
    6) Поиск по одному полю \n \
    7) Поиск по двум полям \n \
    8) ПУПУПУ \n ")


def extra_menu():
    print(Fore.MAGENTA + "Выберите формат заполнения файла: \n\
    1) Заполнить файл самостоятельно \n\
    2) Заполнить файл рандомными данными \n")


def find_or_create_file(filename: str) -> str:
    default_path = "C:\\Users\\Kdima\\OneDrive\\Desktop\\pycourse\\lab14\\"
    
    if os.path.isabs(filename):
        file_path = filename
    else:
        file_path = os.path.join(default_path, filename)
        
        
    if os.path.exists(file_path):
        return file_path
    else:
        with open(file_path, "wb") as f:
            pass    
        return file_path


def get_strings_from_user(filename: str, n: str):
    exit_code = 0
    
    if v.intValidator(n):
        n = int(n)
    else:
        exit_code = 1
        return exit_code, Fore.RED + f"норм числа вводим, окда?"
    
    
    print("Введите данные в формате: \n \
                name;age:weight: ")
    
    with open(filename, "wb") as file:
        for i in range(n):
            s = input("Введите строку: ")
            name, age, weight = s.split(";") 
            
            if v.strValidator(name):
                name_encoded = name.encode("utf-8")
            else:
                exit_code = 1
                return exit_code, Fore.YELLOW + f"Было записано {i+1} строк(а), ошибка при вводе новой строки"
            
            if v.intValidator(age):
                age = int(age)
            else:
                exit_code = 1
                return exit_code, Fore.YELLOW + f"Было записано {i+1} строк(а), ошибка при вводе новой строки"
            
            if v.floatValidator(weight):
                weight = float(weight)
            else:
                exit_code = 1
                return exit_code, Fore.YELLOW + f"Было записано {i+1} строк(а), ошибка при вводе новой строки"
            
            name_encoded = name_encoded.ljust(32, b'\x00')[:32]
            string = struct.pack('32sif', name_encoded, age, weight)
            file.write(string+b'\n')
            
        return exit_code, Fore.GREEN + "Строки в файл записаны успешно"
        

def show_table(filename: str):
    with open(filename, "rb") as binary_file:
        c = 0
        while True:
            data = binary_file.read(41)
            data = data[:-1]
            
            if not data:
                break
            
            name_encoded, age, weight = struct.unpack('32sif', data)
            name = name_encoded.decode('utf-8').rstrip('\x00')
            print(f"{c}:  \n \
        name: {name}; \n \
        age: {age}; \n \
        weight: {round(weight,3)}" )
            c += 1
    return 
            
            
def write_string(filename: str, string: str, n: int):
    if n <= 0:
        return 1, "Неверное значние n"
    name, age, weight = string.split(";")
            
    if v.strValidator(name):
        name_encoded = name.encode("utf-8")
        name_encoded = name_encoded.ljust(32, b'\x00')[:32]
    else:
        exit_code = 1
        return exit_code, Fore.RED + f"Не удалось записать строку в файл, неверный формат входных данных"
                                    
    if v.intValidator(age):
        age = int(age)
    else:
        exit_code = 1
        return exit_code, Fore.RED + f"Не удалось записать строку в файл, неверный формат входных данных"
            
    if v.floatValidator(weight):
        weight = float(weight)
    else:
        exit_code = 1
        return exit_code, Fore.RED + f"Не удалось записать строку в файл, неверный формат входных данных"
    
    
    exit_code = 0
    with open(filename, "rb") as file:
        lines = 0
        for _ in file:
            lines += 1
            
            
    if n >= lines:
        
        with open(filename, "ab") as file:

            string = struct.pack('20sif', name_encoded, age, weight)
            file.write(string+b'\n')
       
        return exit_code, Fore.GREEN + "Строка успешно записана"
    
    else:
        position = (n-1)*41
        
        with open(filename, "r+b") as f:
            current_position = 0
            while current_position < position:
                line = f.read(41)  
                if not line:
                    break
                
                current_position += 41

            start_shift_position = f.tell()

            while line:

                next_line = f.read(41)

                f.seek(start_shift_position)
                f.write(line)
                
                start_shift_position += 41
                line = next_line

            f.seek(position)
        
        with open(filename, "r+b") as file:
            file.seek(position)
            string = struct.pack('32sif', name_encoded, age, weight)
            file.write(string + b'\n')                
        
        return exit_code, Fore.GREEN + "Строка успешно записана"
    
    
def delete_current_line(filename: str, n: str):
    exit_code = 0
    
    if v.intValidator(n):
        n = int(n)
    else:
        exit_code = 1
        return exit_code, Fore.RED + f"Не удалось удалить строку в файл, неверный формат входных данных"
    
    
    with open(filename, "r+b") as file:
        position = (n-1)*41
        file.seek(0,2)
        file_size = file.tell()
        
        if file_size // 41 < n:
            exit_code = 1
            return exit_code, Fore.YELLOW + "Такой строки не существует, но ок, я ее удалил🤡"
        
        
        while True:
            lower_line = position + 41
            file.seek(lower_line)
            s = file.read(41)
            if not s:
                break 
            file.seek(position)
            file.write(s)
            position = lower_line
        
        
        new_size = file_size - 41
        file.truncate(new_size)
        
    return exit_code, Fore.GREEN + "Строка успешно удалена"


def find_by_one_and_show(filename: str, mw: str):
    eps = 1e-5
    
    if v.floatValidator(mw):
        mw = float(mw)
    else:
        print(Fore.RED + f"Сорян, не нашел ничего на твой говно-запрос")
        return 
    
    
    with open(filename, "rb") as binary_file:
        c = 0
        while True:
            data = binary_file.read(41)
            data = data[:-1]
            
            if not data:
                break
            
            name_encoded, age, weight = struct.unpack('32sif', data)
            name = name_encoded.decode('utf-8').rstrip('\x00')
            
            if weight - mw > eps:
                print(f"{c}:  \n \
        name: {name}; \n \
        age: {age}; \n \
        weight: {round(weight,3)}" )
            c += 1
            
            
def find_by_two_and_show(filename: str, mw: str, ma: str):
    eps = 1e-5
    
    if v.floatValidator(mw):
        mw = float(mw)
    else:
        print(Fore.RED + f"Сорян, не нашел ничего на твой говно-запрос")
        return 
    
    
    if v.intValidator(ma):
        ma = float(ma)
    else:
        print(Fore.RED + f"Сорян, не нашел ничего на твой говно-запрос")
        return 
    
    
    with open(filename, "rb") as binary_file:
        c = 0
        while True:
            data = binary_file.read(41)
            data = data[:-1]
            
            if not data:
                break
            name_encoded, age, weight = struct.unpack('32sif', data)
            name = name_encoded.decode('utf-8').rstrip('\x00')
            if (weight - mw > eps) and age > ma:
                print(f"{c}:  \n \
        name: {name}; \n \
        age: {age}; \n \
        weight: {round(weight,3)}" )
            c += 1
            
            
if __name__ == "__main__":
    #find_or_create_file("DB.bin")
    #delete_current_line("lab14/DB.bin", 5)
    #write_string("lab14/DB.bin", "Cris;15;24.5", 7)
    #show_table("lab14/DB.bin")
    #find_by_one_and_show("lab14/DB.bin", 40)
    #find_by_two_and_show("lab14/DB.bin", 70, 30)
    pass