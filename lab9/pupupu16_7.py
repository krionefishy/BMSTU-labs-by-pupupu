from pupupu16_main import fill_matrix, print_matrix
x: int = int(input("Введите x:"))
y: int = int(input("Введите y:"))
z: int = int(input("Введите z:"))

if any(j < 0 for j in [x,y,z]):
    print("x y z должны быть больше 0")
else:
    dct = {"x": x, "y": y, "z": z}
    pu = sorted(dct, key = lambda x: dct[x], reverse = True)
    matr = []
    for i in range(x):
        temp = fill_matrix(y,z,[])
        matr.append(temp)
    if pu[0] == "x":
        idx = x // 2
        print_matrix(matr[idx])
    if pu[0] == "z":
        idx = z // 2
        newm = []
        for j in range(y):
            temp = []
            for i in range(x):
                temp.append(matr[i][j][idx])
            newm.append(temp)
        print_matrix(newm)
    if pu[0] == "y":
        idx = y // 2
        newm = []
        for j in range(z-1,-1,-1):
            temp = []
            for i in range(x):
                temp.append(matr[i][idx][j])
            newm.append(temp)
        print_matrix(newm)