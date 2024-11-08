# Задание 4
# Подготовил Кошеваров Дмитрий ИУ7-16Б
# ввод данных
from pupupu15_main import print_matrix
n: int = int(input('Введите количество строк и столбцов: '))
if n <= 0: # проверка ввода
    print('Wrong input')
else:
    matrix : list[list[int]] = [] # объявление матрицы
    for i in range(n): # заполнение матрицы 
        matrix.append(list(map(int, input('Введите элементы матрицы через пробел: ').split())))
    jmin: int = 0
    jmax: int = 0
    mn: int = 1e5
    mx: int = 0
    
    for i in range(n): # проход по строкам матрицы
        temp = 0
        for j in range(n):
            temp += matrix[j][i]
        if temp > mx: # проверка на максимум
            mx = temp
            jmax = i 
        if temp < mn: # проверка на минимум
            mn = temp
            jmin = i
            
    for i in range(n): # меняем местами столбцы
        matrix[i][jmin], matrix[i][jmax] = matrix[i][jmax], matrix[i][jmin]
    # output
    print("Измененная матрица")
    print_matrix(matrix)  
    