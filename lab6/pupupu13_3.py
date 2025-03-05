# Задание 2а
# Ввод данных
s = list(map(float, input('Введите элементы списка через пробел: ').split()))
ind = int(input('Введите индекс вставки: '))
# проверки
if ind > len(s) or len(s) == 0 or ind < 0:
    print('Введите корректный индекс')
else:
    s.pop(ind)
    print(s) # вывод данных