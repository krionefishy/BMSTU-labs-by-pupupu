# Задание 6
# Подготовил Кошеваров Дмитрий ИУ7-16Б
#
from pupupu16_main import print_matrix_for_strings, fill_matrix
import string 

sogl: set = set(string.ascii_letters.lower()).difference(('a','e','o','u','i')) 
glas: set = ('a','e','o','u','i')
n: int = int(input("Введите количество строк: "))
m: int = int(input("Введите количество столбцов: "))

if n <= 0 or m <= 0:
    print("Введите корректные данные")
else:
    matr: list[list[str]] = fill_matrix(n,m,[], True)
    for i in range(n):
        for j in range(m):
            if matr[i][j].lower() in sogl:
                matr[i][j] = matr[i][j].upper()
            if matr[i][j].lower() in glas:
                matr[i][j] = matr[i][j].lower()
    print("Измененная матрица")
    print_matrix_for_strings(matr)