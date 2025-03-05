# задание 3
# ввод данных
s = list(map(int, input('Введите элементы списка через пробел: ').split()))
k = int(input("Введите K-й номер: "))
# проверки 
if len(s) == 0 or k <= 0:
    print('Введите корректные данные')
else:
    if len(s) == 1:
        print(s[0])
    else:
        n = 0
        ind = None 
        for i in range(1,len(s)-1):
            if (s[i-1] < s[i] and s[i] > s[i+1]) or (s[i-1] > s[i] and s[i] < s[i+1]):
                n += 1
                if n == k:
                    
                    ind = i
                    break
        # вывод данных
        if n >= k:
            print(f'Точка экстремума: {s[ind]}, стоит по индексу {ind}')
        else:
            print('У списка нет точки экстремума')
            
