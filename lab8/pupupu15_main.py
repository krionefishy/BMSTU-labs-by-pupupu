from math import *
def print_matrix(ma):
    for i in range(len(ma)):
        for j in range(len(ma[i])):
            print(str(ma[i][j]).ljust(3), end = ' ')
        print()
        
def prime(x: int):
    if x == 1:
        return False
    for i in range(2,round(sqrt(x)) + 1):
        if x % i == 0:
            return False
    else:
        return True
    
def print_stolb(matr: list[list], j: int):
    for i in range(len(matr)):
        print(matr[i][j])