from faker import Faker
from random import *
import struct


def fill_data(filename: str, n: int):
    with open(filename, "wb") as binary_file:      
        for i in range(n):
            idx = i
            name = Faker().name().replace("\n", " ")
            age = randint(20,70)
            weight = randint(30,100) + random()
            name_encoded = name.encode("utf-8")
            name_encoded = name_encoded.ljust(32, b'\x00')[:32]
            string = struct.pack('32sif',name_encoded, age, weight)
            binary_file.write(string + b'\n')
                   
    return   

    
if __name__ == "__main__":
    #fill_data("C:\\Users\\Kdima\\OneDrive\\Desktop\\pycourse\\lab14\\DB.bin", 10)
    pass 