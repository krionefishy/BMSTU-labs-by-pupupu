from typing import Any

def print_matrix(ma: list[list[int]]):
    "вывод матрицы построчно"
    for i in range(len(ma)):
        for j in range(len(ma[i])):
            print(f"{ma[i][j]:>10g}", end = ' ')
        print()


def fill_matrix(n:int,m:int,matr: list, is_string = False) -> list[list]:
    'заполение матрицы построчно'
    if is_string:
        for i in range(n): # Заполнение матрицы
            s = list(input("Введите строку для матрицы: ").split())
            if len(s) != m:
                raise Exception(f"Введите {m} символов")
            else:
                matr.append(s)
    else:
        for i in range(n): # Заполнение матрицы
            s = list(map(int, input("Введите строку для матрицы: ").split()))
            if len(s) != m:
                raise Exception(f"Введите {m} символов")
            else:
                matr.append(s)
    return matr


def rotate_right(matr: list) -> list[list]:
    'транспонирование матрицы вправо'
    for i in range(len(matr)):
        for j in range(i+1):
            matr[i][j], matr[j][i] = matr[j][i], matr[i][j]
    for i in range(len(matr)):
        for j in range(len(matr)//2):
            matr[i][j], matr[i][len(matr) - j - 1] = matr[i][len(matr) - j - 1], matr[i][j]
    
    return matr


def rotate_left(matr: list) -> list[list]:
    'транспонирование матрицы влево'
    for i in range(len(matr)):
        for j in range(len(matr)//2):
            matr[i][j], matr[i][len(matr) - j - 1] = matr[i][len(matr) - j - 1], matr[i][j]
    for i in range(len(matr)):
        for j in range(i+1):
            matr[i][j], matr[j][i] = matr[j][i], matr[i][j]
    
    return matr


def nums_mult_matrix(matr: list, nums: list[int]):
    'умножение столбцов матрицы на числа'
    c = 0
    for j in range(len(matr[0])):
        for i in range(len(matr)):
            if nums[c] == 0:
                continue
            else:
                matr[i][j] = matr[i][j] * nums[c]
        c += 1
    
    return matr



def find_stolb(matr: list[list[Any]], l: int):
    'вывод конкретного столбца матрицы'
    res = []
    for i in range(len(matr)):
        res.append(matr[i][l])
    return res


def matrixmult(A: list[list[int]], B: list[list[int]]):
    'умножение матриц'
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    if cols_A != rows_B:
      print("Невозможно выполнить умножение матриц")
      return
    C = [[0 for i in range(cols_B)] for j in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]
    return C


def print_matrix_for_strings(matr: list[list[str]]):
    'вывод матрицы элементы которой - строки'
    for i in range(len(matr)):
        for j in range(len(matr[0])):
            print(matr[i][j].rjust(3), end=" ")
        print()


if __name__ == "__main__":
    pass

