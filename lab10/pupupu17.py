from prettytable import PrettyTable
from tests import test
# Лабораторная работа 10
# Подготовил: Кошеваров Дмитрий ИУ7-16Б
# Назначение программы: Вычисление приближенного интеграла двумя способами

# Объявляем функцию
def func(x: float) -> float:
    return x**3 + x - 1

# Первообразная функции
def perv(x: float) -> float:
    return x**4/4 + x**2/2 - x

# метод левых прямоугольников
def integral_left_rect(start: float, end: float, n: int) -> float:
    res: float = 0
    step: float = (end - start) / n
    flag = False
    for i in range(int(n)):
        try:
            res += step*func(start + step*i)
            flag = True
        except: # если не получится посчитать интеграл, то обрабатываем ошибку и возвращаем -
            ValueError
            ZeroDivisionError
            raise Exception("увы")
        if flag == False:
            return "-"
        flag = True
    return res 

# метод параболы
def simpsons(start: float, end: float, n: int) -> float:
    res: float = 0
    step: float = (end - start) / n
    flag = False
    for i in range(int(n)):
        try:
            temp = (step / 6) * (func(start + step*i) + 4 * func((start + step*i + start + step*(i+1)) / 2) + func(start + step*(i+1)))
            res += temp
            flag = True
        except: # если не получится посчитать интеграл, то обрабатываем ошибку и возвращаем -
            ValueError
            ZeroDivisionError
            raise Exception("Увы")
        if flag == False:
            return "-"
        flag = False
    return res 

# поиск количества разбиений, при котором будет точность eps 
def binary_search(method, start: int, end: int, left = 2, right = 1000000, eps = 1e-5):
    if abs(left - right) < 2:
        return 0,0
    else:
        mid = (left + right) // 2
        delta = abs(method(start, end, mid) - method(start, end, mid*2))
        if delta > eps:
            left = mid
            binary_search(method, start, end, left, right, eps)
        else:
            return mid, method(start, end, mid)
    return 0,0
    
try : # Ввод данных
    start: float = float(input("Введите начало отрезка: "))
    end: float = float(input("Введите конец отрезка: "))
    n1: int = int(input("Введите количество разбиений N1: "))
    n2: int = int(input("Введите количество разбиений N2: "))
    eps: float = float(input("Введите точность: "))
except: # Если введены неправильные данные
    ValueError
    raise Exception("Иди нахуй отсюда, строки он мне блять вводит")

if not test(start, end, n1, n2, eps): # проверка 
    print("Введены неправильные значение, убедитесь, что:\n стартовое значение меньше конечного \n N1 и N2 > 0 \n eps > 0")
else:
    integral: float = perv(end) - perv(start) # вычисление интеграла по формуле лейбница
    table = PrettyTable() # создание табоицы
    table.field_names = ["", "N1", "N2", "относительная погрешность", "абсолютная погрешность"] # шапка таблицы

    
    i1: float = round(integral_left_rect(start, end, n1), 3)
    i2: float = round(integral_left_rect(start, end, n2), 3)
    temp1 = [i for i in (i1, i2) if i != '-'] # находим значение при котором не равно -
    m1_rel = sorted(temp1, key = lambda x: abs(integral - x))[0] if len(temp1) > 0 else "-"
    # добавляем строку таблицы
    table.add_row(["Метод левых прямоугольников", i1, i2, f"{((1 - (m1_rel / integral)) * 100):3f}%", f"{abs(m1_rel - integral):3g}"], divider=True)

    i3: float = round(simpsons(start, end, n1), 3)
    i4: float = round(simpsons(start, end, n2), 3)
    temp2 = [i for i in (i3, i4) if i != "-"] # находим значение при котором не равно -
    # добавляем строку таблицы
    m2_rel: float = sorted(temp2, key = lambda x: abs(integral - x))[0] if len(temp2) > 0 else "-"
    table.add_row(["Метод парабол", i3, i4,f"{((1 - (m2_rel / integral)) * 100):3f}%", f"{abs(m2_rel - integral):3g}"])
    # вывод данных
    print(table)
    if abs(integral - m1_rel) < abs(integral - m2_rel): # нахождение наиболее точного значения и способа и вывод данных
        print("Наиболее точный метод - Метод левых прямоугольников")
        print(f"Приближенное значение интеграла - {m1_rel}")
        print("Наименее точное значение получается при методе - параболы")
        n3, res = binary_search(simpsons, start, end, eps)
        if n3 != None and res != None:
            print(f"Приближенное значение интеграла достигается при {n3} количестве разбиений")
            print(f"Приближенное значение интеграла равно {res}")
    else:
        print("Наиболее точной метод - Метод симпсонов")
        print(f"Приближенное значение интеграла - {m2_rel}")
        n3, res = binary_search(integral_left_rect, start, end, eps)
        if n3 != 0 and res != 0:
            print(f"Приближенное значение интеграла достигается при {n3} количестве разбиений")
            print(f"Приближенное значение интеграла равно {res}")
        
    