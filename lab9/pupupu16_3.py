# задание 3 
# Подготовил Кошеваров Дмитрий ИУ7-16Б
from pupupu16_main import print_matrix, fill_matrix, find_stolb, nums_mult_matrix
na:int = int(input("Введите количество строк матрицы A: "))
m:int = int(input("Введите количество столбцов матрицы A и B: "))
nb:int = int(input("Введите количество строк матрицы B: "))
if any(j <= 0 for j in [na,na,m]):
    print("Введите корректные данные столбцов и строк")
else:
    matra: list[list[int]] = fill_matrix(na,m,[])# объявление матрицы D 
    matrb: list[list[int]] = fill_matrix(na,m,[]) # объявление матрицы Z      
    
    s: list[float] = [(sum(find_stolb(matrb, i)) / 2)  for i in range(m)]

    for j in range(m):
        c = 0
        for i in range(na):
            if matra[i][j] > s[j]:
                c += 1
        s[j] = c
    print("Масиив s")
    print(s)
    # Преобразование матрицы
    matrb = nums_mult_matrix(matrb, s)

    # output 
    print(f"Матрица A:")
    print_matrix(matra)
    print(f"Матрица B:")
    print_matrix(matrb)
