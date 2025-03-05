# Выполнил: Кошеваров Дмитрий 
# Группа: ИУ7-16Б
# Название: построение графика в консоли по таблице вариант 45
from math import sqrt
# ВВОД ДАННЫХ 
start = float(input('Введите стартовое значение: '))
h = float(input('Введите шаг икса: '))
end = float(input('Введите конечное значение: '))
e = 1e-20
width = int(input('Введите ширину: '))
p = start
if p >= end or h <= 0 or h >= 1e100 or end > 1e+17 or width >= 140:
    print('Введите корректные данные')
else:
    print('+' + '-' * 48 + "+",
        '|      X     |        y1       |        y2       |',
        '|------------+-----------------+-----------------|', sep='\n')

    # f1 =  2.3p**4 + 1.5p**3 + 6.45p**2 - 24.647p + 12 
    # f2 = 21.987 - 10.112 * 2**p 


    # Определяем первую функцию
    y1 = 2.3*(p**4) + 1.5*(p**3) +6.45*(p**2) - 24.647*p + 12
    # Определяем вторую функцию
    y2 = 21.987 - 10.112 * (2**p)

    # находим кол во итерций 
    iter_count = round((end-p) / h)


    y1min = y2min = 1e10
    y2max = -1e11
    # проход цикла и вычисление значений y 
    for i in range(iter_count):
        p += h 
        if p > end:
            break
        else:
            y1 = 2.3*(p**4) + 1.5*(p**3) +6.45*(p**2) - 24.647*p + 12
            if y1 < y1min:
                y1min = y1
            y2 = 21.987 - 10.112 * (2**p) - 5
            if y2 < y2min:
                y2min = y2
            if y2max < y2:
                y2max = y2
            print(f'| {p:^10.2f}| {y1:^15.3f} | {y2:^15.3g} |')

    print('+' + '-' * 48 + "+")

    print(f'Минимальное значение y1: {y1min:6.6g}\nМииниальное значение y2: {y2min:6.6g}')
    ex = sqrt(abs(y1min * y2min))
    print(f'Доп задание: {ex:6.6g}')


    dot_count = int(input('Введите количество засечек на Оy от 4 до 8:'))
    if not (4 <= dot_count <= 8):
        print('Введенное количество точек не соответсвует условию')

        
    x = start
    zero_y = round(-y2min * width / (y2max - y2min))

    # проставление точек на оси
    print(" " * 8, end="")
    for i in range(dot_count):
        print(f"{y2min+(y2max-y2min)*i/(dot_count-1):<{width//(dot_count-1)}.3f}", end="")
    print()

    print("-" * (15 + width) + "> y")

    for i in range(iter_count+1):
        y = 21.987 - 10.112 * (2**x) - 5
        graph_y = round((y - y2min)*width / (y2max-y2min)) # нахождение относительной координаты y
        
        if (zero_y < 0):
            print(f"{x:^6.3f} |{' ' * graph_y}*{' ' * (width-graph_y)}")
        else:
            if zero_y == graph_y:
                print(f"{x:^6.2f} |{' ' * graph_y}*{' ' * (width-graph_y)}")
            elif zero_y >  graph_y:
                print(f"{x:^6.2f} |{' ' * graph_y}*{' ' * (zero_y - graph_y - 1)}|{' '* (width - zero_y)}")
            else:
                print(f"{x:^6.2f} |{' ' * zero_y}|{' ' * (graph_y - zero_y - 1)}*{' ' *(width-graph_y)}")

        # проставление точек
            
        x += h
