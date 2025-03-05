# Задание 2
# Подготовил Кошеваров Дмитрий ИУ7-16Б
from pupupu16_main import print_matrix, fill_matrix, rotate_left, rotate_right
# ввод данных 
n: int = int(input("Введите кол во строк и столбцов: "))
if n <= 0:
    print("Введите корректные данные")
else:
    matr: list[list[int]] = fill_matrix(n,n,[]) # заполнение матрицы
    # output 
    print(f"Исходная матрица:")
    print_matrix(matr)
    
    
    matr = rotate_right(matr)
    print(f"Матрица повернутая на 90 градусов в право:")
    print_matrix(matr)
    
    matr = rotate_left(matr)
    print(f"матрица повернутая на 90 градусов влево: ")
    print_matrix(matr)