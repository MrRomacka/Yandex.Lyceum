newcode = str(input("Введите код на проверку: "))

if len(newcode) != 3:
    print("Длина кода не соответствует требованиям.")
    print(newcode[2])
else:
    if (newcode[0] == newcode[2]) or (newcode[1] == newcode[2]) or (newcode[1] == newcode[0]):
        if (newcode[0] == newcode[1] == newcode[2]):
            print("Все цифры кода одинаковые.")
        else:
            print("Две цифры кода одинаковые.")
    else:
        print("ОК")

