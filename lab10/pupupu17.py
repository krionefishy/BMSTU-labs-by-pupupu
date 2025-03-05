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
def integral_left_rect(start: float, end: float, n: int):
    res: float = 0
    step: float = (end - start) / n
    flag = False
    for i in range(int(n)):
        res += step*func(start + step*i)
        flag = True
        if flag == False:
            return "-"
        flag = True
    return res 


# метод параболы
def simpsons(start: float, end: float, n: int):
    res: float = 0
    step: float = (end - start) / n
    flag = False
    for i in range(int(n)):
        temp = (step / 6) * (func(start + step*i) + 4 * func((start + step*i + start + step*(i+1)) / 2) + func(start + step*(i+1)))
        res += temp
        flag = True
        if flag == False:
            return "-"
        flag = False
    return res 


# поиск количества разбиений, при котором будет точность eps 
def binary_search(method, start: int, end: int, n: int, eps: float = 1e-5):
    temp = method(start, end, n)
    curr = n
    if curr > 1e8:
        return 0, 0
    k = method(start, end, curr * 2)
    curr *= 2
    while abs(temp - k) > eps:
        temp = k
        curr *= 2
        k = method(start, end, curr)
    return curr, temp
    
    
def otn(x):
    global integral
    return (1 - (x / integral)) * 100

def absolute(x):
    global integral
    return abs(x - integral)
    
try : # Ввод данных
    start: float = float(input("Введите начало отрезка: "))
    end: float = float(input("Введите конец отрезка: "))
    n1: int = int(input("Введите количество разбиений N1: "))
    n2: int = int(input("Введите количество разбиений N2: "))
    eps: float = float(input("Введите точность: "))
except: # Если введены неправильные данные
    ValueError
    raise Exception("Значения минус вайбные")


if not test(start, end, n1, n2, eps): # проверка 
    print("Введены неправильные значение, убедитесь, что:\n стартовое значение меньше конечного \n N1 и N2 > 0 \n eps > 0")
else:
    integral: float = perv(end) - perv(start) # вычисление интеграла по формуле лейбница
    table = PrettyTable() # создание табоицы
    table.field_names = ["", "N1","отн погр N1","абс погр N1", "N2","отн погр N2", "абс погр N2"] # шапка таблицы

    
    i1: float = round(integral_left_rect(start, end, n1), 3)
    i2: float = round(integral_left_rect(start, end, n2), 3)
    temp1 = [i for i in (i1, i2) if i != '-'] # находим значение при котором не равно -
    
    m1_rel = sorted(temp1, key = lambda x: abs(integral - x))[0] if len(temp1) > 0 else "-"
    # добавляем строку таблицы
    table.add_row(["Метод левых прямоугольников", i1,f"{otn(i1):3f}%", f"{absolute(i1):3f}", i2, f"{otn(i2):3f}%", f"{absolute(i2):3g}"], divider=True)

    i3: float = round(simpsons(start, end, n1), 3)
    i4: float = round(simpsons(start, end, n2), 3)
    temp2 = [i for i in (i3, i4) if i != "-"] # находим значение при котором не равно -
    
    m2_rel: float = sorted(temp2, key = lambda x: abs(integral - x))[0] if len(temp2) > 0 else "-"
    # добавляем строку таблицы
    table.add_row(["Метод парабол", i3,f"{otn(i3):3f}%", f"{absolute(i3):3f}", i4, f"{otn(i4):3f}%", f"{absolute(i4):3f}"])
    
    # вывод данных
    print(table)
    if abs(integral - m2_rel) - abs(integral - m1_rel) > eps : # нахождение наиболее точного значения и способа и вывод данных
        print("Наиболее точный метод - Метод левых прямоугольников")
        print(f"Приближенное значение интеграла - {m1_rel}")
        print("Наименее точное значение получается при методе - параболы")
        n3, res = binary_search(simpsons, start, end, n2 ,eps)
        if n3 != 0 and res != 0:
            print(f"Приближенное значение интеграла достигается при {n3} количестве разбиений")
            print(f"Приближенное значение интеграла равно {res}")
        else:
            print("Вычислить нельзя")

    else:
        print("Наиболее точной метод - Метод симпсонов")
        print(f"Приближенное значение интеграла - {m2_rel}")
        print("Наименее точное значение получается при методе левых прямоугольников")
        n3, res = binary_search(integral_left_rect, start, end, n2 ,eps)
        if n3 != 0 and res != 0:
            print(f"Приближенное значение интеграла достигается при {n3} количестве разбиений")
            print(f"Приближенное значение интеграла равно {res}")
        else:
            print("Вычислить нельзя")
            
        