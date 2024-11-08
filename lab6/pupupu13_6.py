# Задание 4 Вариант 6
# ввод данных
s = list(map(int, input('Введите элементы списка через пробел: ').split()))
if len(s) < 3:
    print('Введите корректные данные')
else:
    idxs = 0
    idxe = 0
    is_posl = False
    f = False
    for i in range(2,len(s)):
        if is_posl:
            if s[idxe]*s[idxe-1] == s[i]:
                idxe += 1
            else:
                is_posl = False
        elif s[i-2] * s[i-1] == s[i]:
            idxs = i - 2
            idxe = i
            is_posl = True

    

    # вывод данных
    print(s[idxs:idxe+1])
    
    
