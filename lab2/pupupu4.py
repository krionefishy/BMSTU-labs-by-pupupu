# Выполнил: Кошеваров Дмитрий
# Группа ИУ7-16Б
# Назначение программы: нахождение y по заданному x
from math import sqrt
# ВВОД ДАННЫХ
x = float(input())


# Проверка введенного x и вычисление соответственной для него функции

if (x >= -6) and (x < 4):
    y = -(x/2)**2 + 4
elif (x >= 4) and (x < 8):
    y = sqrt(x-4)
elif x >= 8:
    y = (x-4)/2
else:
    y = -(x-4) / 2 - 10
print(f'y = {y:5f}')
