a = int(input("Строки: "))
b = int(input("Столбцы: "))
symbol = str(input("Символ: "))
space = " "

print(symbol * b)
for i in range(a - 2):
    print (symbol + space * (b - 2) + symbol)
print(symbol * b)