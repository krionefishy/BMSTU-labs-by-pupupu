# Задание 4 
# Подготовил Кошеваров Дмитрий ИУ7-16Б
from pupupu16_main import print_matrix, fill_matrix
# Вход данных
n:int = int(input("Введите количество строк матрицы D: "))
m:int = int(input("Введите количество столбцов матрицы D: "))
if n <= 0 or m <= 0: # проверка правильности ввода
    print("Введите корректные данные для строк и столбцов")
else:
    matr: list[list[int]] = fill_matrix(n,m,[])         
    lines: list[int] = [] # список строк, у которых надо взять максимум
    countOfMax:int = int(input("Введите количество строк у которых надо найти максимум: ")) # ввод количества строк для максимумов
    
    for i in range(countOfMax):
        s:int = int(input("Введите номер строки: ")) 
        if s >= 0 and s not in lines and s < n: # проверка корректности ввода
            lines.append(s)
            
    if len(lines) == 0: # проверка
        print("Введите корректные данные для массива")
    else:
        localMaxes: list[int] = [] # объявляем массив R 
        for i in lines:
            mx = matr[i][0]
            for j in matr[i][1:]:
                if j > mx:
                    mx = j
            localMaxes.append(mx)
            
        sr: float = sum(localMaxes) / len(localMaxes) # среднее арифметическое
        
        # output
        print("Ваша матрица: ")
        print_matrix(matr)
        print(lines)
        print(f'Список максимумов: {localMaxes}')
        print(f'Среднее значение максимумов: {sr}')