# Задание 2b алгоритмическое решение
# ввод данных
s = list(map(int, input('Введите элементы списка через пробел: ').split()))
ind = int(input('Введите индекс удаления: '))
# проверки
if abs(ind) > len(s) or len(s) == 0 or ind < 0:
    print('Введите корректный индекс')
else:    
    for i in range(ind,len(s)-1):
        s[i] = s[i+1]
        
    s = s[:-1]
    print(s)# вывод данных