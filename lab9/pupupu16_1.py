# Задание 1
# Подготовил Кошеваров Дмитрий ИУ7-16Б
from pupupu16_main import print_matrix
from math import sqrt
n: int = int(input("Введите длину для массивов D и F: "))
if n <= 0:
    print("Введите корректные данные")
else:
    d: list[int] = []
    f: list[int] = []
    # заполнение массивов
    print("Введите элементы для D: ")
    d: list[int] = list(map(int, input().split()))
    print("Введите элементы для F: ")
    f: list[int] = list(map(int, input().split()))
    # заполнение матрицы
    matr: list[int] = []
    s: list[int] = []
    for i in range(n):
        temp = []
        c = 0
        for j in range(n):
            k = d[i]*f[j]
            temp.append(k)
            if sqrt(k) == int(sqrt(k)):
                c += 1
        s.append(c)
        matr.append(temp)
    # output
    print("Ваша матрица:")
    print_matrix(matr)
    print("столбец:")
    for i in s:
        print(i)
        

        