n = int(input())
summa = 0
square = 0

for i in range (n):
    square = 1 / (i + 1) ** 2
    summa = summa + square

result = (3.141592653589793 ** 2) / summa
print(result)