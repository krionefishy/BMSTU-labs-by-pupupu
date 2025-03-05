# Задание 1 вариант 1
# Подготовил Кошеваров Дмитрий ИУ7-16Б
# ввод данных
n: int = int(input('Введите количество строк и столбцов: '))
if n <= 0: # проверка ввода
    print('Wrong input')
else:
    matrix : list[list[int]] = [] # объявление матрицы
    for i in range(n): # заполнение матрицы 
        matrix.append(tuple(map(int, input('Введите элементы матрицы через пробел: ').split())))
    mxmiddle: int = 0
    idx: int = 0
    for i in range(n): # проход по строкам матрицы и нахождение нужной строки
        if mxmiddle < sum(matrix[i]) / n:
            idx = i 
            mxmiddle = sum(matrix[i]) / n
            
    # output
    print(f'Строка с максимальным средним арифетическим: {matrix[idx]}')
    
        