# задание 5
# Подготовил Кошеваров Дмитрий ИУ7-16Б
from pupupu16_main import print_matrix, fill_matrix, matrixmult
# ввод данныъ
na: int = int(input("Введите количество строк A: "))
ma: int = int(input("Введите количество столбцов A: "))
nb: int = int(input("Введите количество строк B: "))
mb: int = int(input("Введите количество столбцов B: "))
if any(j <= 0 for j in [na,nb,ma,mb]):
    print("Введите корректные данные")
else:
    matra:list[list[int]] = fill_matrix(na,ma,[])
    matrb:list[list[int]] = fill_matrix(nb,mb,[])    

    c = matrixmult(matra, matrb)
    # output
    print("Матрица A:")
    print_matrix(matra)
    print("Матрица B:")
    print_matrix(matrb)
    print("Матрица С")
    print_matrix(c)