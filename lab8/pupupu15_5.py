# Задание 5
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
        
    mx: int = 0 # объявляем максимум
    mn: int = 1e5 # объявляем минимум
    for i in range(n):
        for j in range(n):
            if (i < j and i < n - j - 1) or (i < j or i > n - j - 1): # проверка на то, что выше главной диагонали
                mx = max(mx, matrix[i][j])
            if (i < j and i > n - j - 1) or (i > j and i > n - j - 1): # проверка на то, что ниже побочной диагонали
                mn = min(mn, matrix[i][j])
    # output
    print(f"Максимальное значение над главной диагональю: {mx}")
    print(f"Минимальное значение под побочной диагональю {mn}")