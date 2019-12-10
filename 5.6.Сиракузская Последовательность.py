n = int(input('Введите число: '))
count = 0


while n != 1:
    h = n % 2
    count = count + 1
    if h == 0:
        n = n / 2
    else:
        n = n * 3 + 1

print(count)