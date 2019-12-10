Ch1 = float(input("Введите первое число: "))
Ch2 = float(input("Введите второе число: "))
oper = input("Введите желаемую операцию: ")
result = 0

if oper == "+":
    result = Ch1 + Ch2
    print(result)
elif oper == "-":
    result = Ch1 - Ch2
    print(result)
elif oper == "*":
    result = Ch1 * Ch2
    print(result)
elif oper == "/":
    result = Ch1 / Ch2
    print(result)
else:
    print('888888')

