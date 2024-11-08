# Задание 5, вариант 4
s = list(map(int, input("Введите список элементов: ").split()))# ввод данных
if len(s) < 1 and len([i for i in s if i < 0]) < 1:
    print('Введите корректные данные')
else:
    # обявляем минимальный и максимальный элементы
    min_index = max_index = mn = 0
    mx = -1*(1e100)
    # выполняем проход по циклу и меняем значения minot, maxot
    for i in range(1,len(s)):
        if s[i] < 0:
            if s[i] < mn:
                mn = s[i]
                min_index = i
            if s[i] > mx:
                mx = s[i]
                max_index = i

    s[min_index], s[max_index] = s[max_index], s[min_index]
    print(s) # вывод данных