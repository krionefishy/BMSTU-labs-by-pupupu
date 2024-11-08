# Задание 1a 
# ввод данных
s = list(map(int, input('Введите элементы списка через пробел: ').split()))
ind = int(input('Введите индекс вставки: '))
if ind > len(s)  or ind < 0:
    print('Введите корректный индекс')
else:
    el = int(input('Введите элемент для ввода: '))
    # проверки корректности ввода

    if len(s) == 0 and ind == 0:
        s.insert(ind,el)
        print(s) # вывод данных
    else:
        s.insert(ind,el)
        print(s) # вывод данных