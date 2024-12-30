# лабораторная работа 15
# подготовил Кошеваров Дмитрий
# Варианты к заданиям: 5, 3, heapsort

import struct

file_path = "lab15/file3.bin"
numbers = [100, -2, 100,  0, 100, -100, -1, -1]

with open(file_path, "wb") as f:
    for num in numbers:
        f.write(struct.pack("i", num))
        
        
def left(i: int):
    return 2*i + 1


def right(i: int):
    return 2*i + 2

        
def read_from_file(file, n: int):
    file.seek(n * 4)
    number = struct.unpack("i", file.read(4))[0]
    return number

def write_to_file(file, n: int, num: int):
    file.seek(n * 4)
    file.write(struct.pack("i", num))
    
    

def swap(file, i: int,j: int):
    file.seek(i*4)
    pos1 = file.tell()
       
    file.seek(j*4)
    pos2 = file.tell()
    
    file.seek(pos1)
    el1 = file.read(4)
      
    file.seek(pos2)
    el2 = file.read(4)
     
    file.seek(pos2)
    file.write(el1)
      
    file.seek(pos1)
    file.write(el2)
        

def heaplify(file, l: int, i: int):
    largest = i
    left_pos = left(i)
    right_pos = right(i)
    
    if left_pos < l:
        left_elem = read_from_file(file, left_pos)
        root = read_from_file(file, largest)
        if left_elem > root:
            largest = left_pos
            
    if right_pos < l:
        right_elem = read_from_file(file, right_pos)
        root = read_from_file(file, largest)
        if right_elem > root:
            largest = right_pos
    
    if largest != i:
        largest_value = read_from_file(file, largest)
        root = read_from_file(file, i)
        write_to_file(file, i, largest_value)
        write_to_file(file, largest, root)
        heaplify(file, l, largest)
        
        

def heapsort(filename: str):
    with open(filename, "r+b") as file:
        file.seek(0,2)
        n = file.tell()//4
        
        for i in range(n // 2 - 1, -1, -1 ):
            heaplify(file, n, i)

        for i in range(n - 1, 0, - 1):
            root = read_from_file(file, 0)
            end = read_from_file(file, i)
            write_to_file(file, 0, end)
            write_to_file(file, i, root)

            heaplify(file, i, 0)
            
            
heapsort(file_path)

with open(file_path, "rb") as file:
    num = file.read(4)
    while num:
        print((struct.unpack("i", num))[0], end = " ")
        num = file.read(4)