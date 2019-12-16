a = [[0]*10 for i in range(10)]
print(a)
b = [[0]*10]*10
print(b)
c = a.copy()
c[3][5] = 6             #из-за copy изменяется и начальная матрица
print(*a, sep='\n')     #есть deepcopy из import copy
                        #он не даёт изменить начальное