import math

chis = float(input('Введите число: '))

step = math.log(chis, 2)

prove = step * 2 % 2

if prove == 0:
    print(step)
else:
    print('Нет.')