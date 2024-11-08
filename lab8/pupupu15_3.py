# Задание 2 вариант 1
# Подготовил Кошеваров Дмитрий ИУ7-16Б
# ввод данных
from pupupu15_main import prime, print_stolb
n: int = int(input('Введите количество строк и столбцов: '))
if n <= 0: # проверка ввода
    print('Wrong input')
else:
    matrix : list[list[int]] = [] # объявление матрицы
    for i in range(n): # заполнение матрицы 
        matrix.append(tuple(map(int, input('Введите элементы матрицы через пробел: ').split())))
        
    count_prime: int = 0 # объявляем максимальное количество простых чисел
    j_ind: int = 0 # для запоминания индекса столбца
    for i in range(n):
        temp = 0
        for j in range(n):
            if prime(matrix[j][i]): 
                temp += 1
        if temp > count_prime: # сравнение с максимумом
            count_prime = temp 
            j_ind = i 
    # output
    print(f"Больше всего простых чисел в столбце с индексом {j_ind}, кол-во чисел {count_prime}")
    print("Ваш столбец:")
    print_stolb(matrix, j_ind)