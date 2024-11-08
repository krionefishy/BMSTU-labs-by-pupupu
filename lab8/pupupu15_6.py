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
        
    '''matrix = list(zip(*matrix))'''
    for i in range(n): # проход по матрице и изменения положения элементов по маленьким диагоналям
        for j in range(0,i+1):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # output
    print_matrix(matrix)