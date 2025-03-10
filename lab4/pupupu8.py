# Выполнил: Кошеваров Дмитрий
# Группа: ИУ7-16Б
# Назначени программы: Вычисление суммы бесконечной числовой последовательности
# импортируем библиотеку для таблицы
from prettytable import PrettyTable
# задаем шапку таблицы
th = ["№ итерации", 't', 's']
td = []
# ВВОД ДАННЫХ
n = int(input('Введите количество итераций: '))
accuracy = float(input('Введие точность: '))
sh = int(input('Введите шаг печати: '))

# объявляем переменную суммы и сразу записываем туда базовый случай (x = 1)
s = 1
# to_show - номера итераций, которые надо вывести в табличке
to_show = 1 + sh
# объявляем переменную t, которая является нашей следующей итерацией
# (1/1 == 1/1!)
t = 1 / 1
# объявляем счетчик итераций
iter_num = 1

# добавляем в td строку с первой итерацией
td.append((iter_num,t,s))
# создаем таблицу
table = PrettyTable(th)

# Проход цикла while, пока элемент t не меньше заданной точности accuracy
# и iter_num меньше заданного кол-ва итераций
while t >= accuracy and iter_num < n:
    iter_num += 1
    s += t
    if iter_num == to_show:
        to_show += sh
        # добавляем в td строку, которую нужно вывести
        td.append([iter_num, float('{:6.6g}'.format(t)), float('{:6.6g}'.format(s))])
    t /= iter_num 
# создаем копию списка со строками таблицы
td_data = td[:]
# заполняем таблицу
while td_data:
    table.add_row(td_data[0])
    td_data = td_data[1:]
# вывод таблицы
print(table)    
# вывод итоговой суммы и кол-ва итераций
print(f'Сумма бесконечного ряда равна: {s:6.6g}, вычислена за {iter_num} операций')
