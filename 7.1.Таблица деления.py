stolbets = int(input('Столбцы: '))
stroka = int(input("Строки: "))

for i in range (1, stroka + 1):
    for j in range(1, stolbets + 1):
        print(j / i, end='\t')
    print()