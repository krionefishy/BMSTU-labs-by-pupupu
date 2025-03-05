# квадратные уравнения
from math import sqrt
a = float(input('Введите значение коэффициента a: '))
b = float(input('Введите значение коэффициента b: '))
c = float(input('Введите значение коэффициента c: '))
if a == b == c:
    print('x - любое')
else:
    
    if a != 0:
        D = b**2 - 4*a*c
        if D > 0:
            x1 = (-b + sqrt(D))/(2*a)
            x2 = (-b - sqrt(D))/(2*a)
            print(f'Решения уравнения: x1 = {x1:5f}, x2 = {x2:5f}')
        elif D == 0:
            x = -b / (2*a)
            print(f'Решения уравнения: x = {x:5f}')
        else:
            print('Решений нет')
    if a == 0:
        if b != 0 and c != 0:
            x = -c / b
            print(f'Решение уравнения: x = {x:5f}')
        elif b == 0:
            print('Решений нет, график - прямая y = c параллельная Ox')
        elif c == 0:
            print('Решение уравнения: x = 0')
