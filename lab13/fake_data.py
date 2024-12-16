from faker import Faker
from random import *

def fill_with_fake_data(filename, n ):
    with open(filename, "w", encoding="UTF-8") as f: 
        f.write("name;age;address;weight\n")
        for i in range(n):
            idx = str(i)
            name = Faker().name().replace("\n", " ")
            age = str(randint(20,50))
            address = Faker().address().replace("\n", " ")
            weight = str(round(randint(30, 110) + random(), 2))
            l = [idx, name, age, address, weight]
            if i != n-1:
                f.write(";".join(l) + "\n")
            else:
                f.write(";".join(l))
    return       
if __name__ == "__main__":
    fill_with_fake_data("C:\\Users\\Kdima\\OneDrive\\Desktop\\pycourse\\lab13\\DB.txt", 100)