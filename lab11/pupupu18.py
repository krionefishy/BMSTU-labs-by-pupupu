# Лабораторная работа 11
# Изучение методов сортировки 
# (Все равно даже bubblesort на Go будет быстрее большинства сортировок на python xD)
# Подготовил Кошеваров Дмитрий ИУ7-16Б
# Пирамидальная сортировка
# descriptiion in README


from prettytable import PrettyTable
from time import *
from math import log2
from random import randint


def left(i: int):
    return 2*i + 1


def right(i: int):
    return 2*i + 2


def swap(lst: list[int], i: int, j: int):
    lst[i], lst[j] = lst[j], lst[i]
    
    
def heaplify(lst: list[int], i: int, n: int, swaps: int):

    left_elem: int = left(i)
    right_elem: int = right(i)
    largest: int = i
    
    if left_elem < n and lst[left_elem] > lst[largest]:
        largest = left_elem
        
    if right_elem < n and lst[right_elem] > lst[largest]:
        largest = right_elem 
    
    if largest != i:
        swap(lst, largest, i)
        swaps[0] += 1
        heaplify(lst, largest, n, swaps)
        
    
def pop(lst: list[int], n: int, swaps: int):
    if n <= 0:
        return 
    swap(lst, 0, n - 1)
    swaps[0] += 1
    heaplify(lst, 0 , n - 1, swaps)
    

def heapsort(lst: list[int]):
    if len(lst) <= 1:
        return lst, 0
    swaps: list[int] = [0]
    n: int = len(lst)
    for i in range(n // 2 - 1, -1 ,- 1):
        heaplify(lst, i, n, swaps)
    
    for i in range(n - 1, 0 , -1):
        pop(lst, i + 1, swaps)
    
    sorted_lst = lst
    return sorted_lst, swaps[0]


if __name__ == "__main__":
    # Ввод данных
    lst: list[int] = list(map(int, input("Введите элементы списка через пробел: ").split()))
    # Проверка данных
    if len(lst) == 0:
        print("Длинна списка должна быть больше нуля")
    res, co = heapsort(lst)

    # вывод отсортированного списка
    print(f"Ваш отсортированный список - {res}")
    print(f"Количество перестановок - {co}, ожидаемое количество перестановок - {int(len(lst) * log2(len(lst)))}")
    N1 = int(input("введите N: "))
    N2 = int(input("введите N: "))
    N3 = int(input("введите N: "))
    
    # Создание таблицы
    table = PrettyTable()
    table.field_names = ["", "N1 элементов", "N2 элементов", "N3 элементов"]
    table.add_row(["", "Время ms / Перестановки","Время ms / Перестановки","Время ms / Перестановки"], divider = True)

    # Список тестовых списков (просто избавился от миллиона вывозовов функций, переприсваивания значений, новых переменных и говнокодинга)
    test: list[list[int]] = [
        # блок для первого теста
        [i for i in range(N1)],
        [randint(1,1000) for i in range(N1)],
        [i for i in range(N1,0,-1)],

        # блок для 2 теста
        [i for i in range(N2)],
        [randint(1,3000) for i in range(N2)],
        [i for i in range(N2,0,-1)],
        
        # блок для 3 теста
        [i for i in range(N3)],
        [randint(1,8000) for i in range(N3)],
        [i for i in range(N3,0,-1)]
    ]

    names: list[str] = ["Упорядоченный список", "Случайный список", "Упорядоченный список в обратном порядке"]
    for i in range(3):
        temp = [names[i]]
        for j in range(len(test)):
            if j % 3 == i:
                start = time()
                _ ,counter = heapsort(test[j])
                end = time()
                temp.append(f"{(end - start)*(10**6):4f}/{counter}")
        table.add_row(temp, divider = True)
        
    print(table)
