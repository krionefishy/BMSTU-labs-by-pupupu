# Задание 4 вариант 2
# Подготовил Кошеваров Дмитрий ИУ7-16Б
# ввод данных
n = int(input('Введите кол во элементов '))
lst = []
for i in range(n):
    lst.append(input('Введите элемент '))
if len(lst) == 0:
    print('Длинна списка должна быть больше нуля')
else:
    res = lst[:] # копирование списка
    for i in range(len(res)): # проход по списку
        for j in range(len(res[i])): # проход по элементу, если встретили гласную маленькую, то меняем
            if res[i][j] in 'aeuoiy':
                res[i] = res[i].replace(res[i][j], res[i][j].upper())
    # вывод данных     
    print(f'Измененный массив: {res}')
