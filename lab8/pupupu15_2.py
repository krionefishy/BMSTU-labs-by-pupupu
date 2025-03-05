# Задание 2
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
        
    mxcootr,idx1,idx2 = 0,0,0
    mncootr = 1e5
    for i in range(n): # проход по строкам матрицы
        temp = 0 # счетчик количества подходящих элементов 
        for j in range(n):
            if matrix[i][j] < 0 :
                temp += 1
        if mxcootr < temp: # проверка на максимум
            mxcootr = temp
            idx1 = i 
        if mncootr < temp: # проверка на минимум
            mncootr = temp
            idx2 = i 
    matrix[idx1], matrix[idx2] = matrix[idx2], matrix[idx1] # меняем строки местами
    
    # output
    print_matrix(matrix)
