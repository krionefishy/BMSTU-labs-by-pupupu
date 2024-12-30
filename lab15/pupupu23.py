# лабораторная работа 15
# подготовил Кошеваров Дмитрий
# Варианты к заданиям: 5, 3, heapsort
import struct
import random

def remove_negatives(file_path: str):
    RECORD_SIZE = 4
    read_pointer = 0
    pos = 0

    with open(file_path, "r+b") as f:
        num = f.read(RECORD_SIZE)
        while num:
            number = struct.unpack("i", num)[0]
            print(number)
            if number >= 0:
                f.seek(pos)
                f.write(struct.pack("i", number))
                pos += RECORD_SIZE

            read_pointer += RECORD_SIZE
            f.seek(read_pointer)
            num = f.read(RECORD_SIZE)
        f.truncate(pos)



file_path = "lab15/file.bin"
numbers = [random.randint(-100,100) for _ in range(15)]
with open(file_path, "wb") as f:
    for num in numbers:
        f.write(struct.pack("i", num))
print("До удаления отрицательных чисел:", *numbers)
remove_negatives(file_path)

with open(file_path, "rb") as f:
    updated_numbers = []
    num = f.read(4)
    while num:
        updated_numbers.append(struct.unpack("i", num)[0])
        num = f.read(4)
print("После удаления:", *updated_numbers)


