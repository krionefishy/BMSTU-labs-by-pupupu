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


def left(i):
    return 2*i + 1


def right(i):
    return 2*i + 2


def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]
    
    
def heaplify(lst, i, n, swaps):

    left_elem = left(i)
    right_elem = right(i)
    largest = i
    
    if left_elem < n and lst[left_elem] > lst[largest]:
        largest = left_elem
        
    if right_elem < n and lst[right_elem] > lst[largest]:
        largest = right_elem 
    
    if largest != i:
        swap(lst, largest, i)
        swaps[0] += 1
        heaplify(lst, largest, n, swaps)
        
    
def pop(lst, n, swaps):
    if n <= 0:
        return 
    swap(lst, 0, n - 1)
    swaps[0] += 1
    heaplify(lst, 0 , n - 1, swaps)
    

def heapsort(lst):
    swaps = [0]
    n = len(lst)
    for i in range(n // 2 - 1, -1 ,- 1):
        heaplify(lst, i, n, swaps)
    
    for i in range(n - 1, 0 , -1):
        pop(lst, i + 1, swaps)
        
    return swaps[0]


# Ввод данных
lst = list(map(int, input("Введите элементы списка через пробел: ").split()))
# Проверка данных
if len(lst) == 0:
    print("Длинна списка должна быть больше нуля")
co = heapsort(lst)

# вывод отсортированного списка
print(f"Ваш отсортированный список - {lst}")
print(f"Количество перестановок - {co}, ожидаемое количество перестановок - {int(len(lst) * log2(len(lst)))}")

# Создание таблицы
table = PrettyTable()
table.field_names = ["", "1000 элементов", "3000 элементов", "8000 элементов"]
table.add_row(["", "Время / Перестановки","Время / Перестановки","Время / Перестановки"], divider = True)

# Список тестовых списков (просто избавился от миллиона вывозовов функций, переприсваивания значений, новых переменных и говнокодинга)
test = [
    # блок для первого теста
    [i for i in range(1000)],
    [randint(1,1000) for i in range(1000)],
    [i for i in range(1000,0,-1)],

    # блок для 2 теста
    [i for i in range(3000)],
    [randint(1,3000) for i in range(3000)],
    [i for i in range(3000,0,-1)],
    
    # блок для 3 теста
    [i for i in range(8000)],
    [randint(1,8000) for i in range(8000)],
    [i for i in range(8000,0,-1)]
]

names = ["Упорядоченный список", "Случайный список", "Упорядоченный список в обратном порядке"]
for i in range(3):
    temp = [names[i]]
    for j in range(len(test)):
        if j % 3 == i:
            start = time()
            counter = heapsort(test[j])
            end = time()
            temp.append(f"{end - start:4f}/{counter}")
    table.add_row(temp, divider = True)
    
print(table)
