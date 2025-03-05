# лабораторная работа 15
# подготовил Кошеваров Дмитрий
# Варианты к заданиям: 5, 3, heapsort
import struct
file_path = "lab15/file2.bin"
numbers = [0]
with open(file_path, "wb") as f:
    for num in numbers:
        f.write(struct.pack("i", num))
        
        
with open(file_path, "rb") as file: # запоминаем позиции элементов, которые нужно удвоить
    n = 0
    positions_to_delete = []
    num = file.read(4)
    while num:
        current = struct.unpack("i", num)[0]
        if current % 2 != 0:
            positions_to_delete.append(n)
        n += 1
        num = file.read(4)
    
    
def add_line(filename: str, n: int):
    with open(filename, "r+b") as file:
        # добавили еще одну строку, чтобы сделать сдвиг
        file.seek(0,2)
        file.seek(file.tell()-4)
        lower_line = file.read(4)
        file.write(lower_line)
        # сдвиг всех строк вниз на одну и копирование нужной строки вниз
        file.seek(n*4)
        current = file.read(4)
        next_line = file.read(4)
        while next_line:
            file.seek(file.tell()-4)
            file.write(current)
            current = next_line
            next_line = file.read(4)
                        
        file.seek(n*4)
        num = struct.unpack("i", file.read(4))[0]        
        file.write(struct.pack("i", num*2))


for i in positions_to_delete[::-1]: 
    add_line(file_path, i)


with open(file_path, "rb") as file:
    num = file.read(4)
    while num:
        print((struct.unpack("i", num))[0], end = " ")
        num = file.read(4)