loginname=input("Введите желаемый логин: ")
reserveemail=input("Введите резервный адрес: ")

if "@" in loginname:
    if "@" in reserveemail:
        print('Некорректный логин')
    else:
        print("Некорректные логин и адрес")
else:
    if "@" in reserveemail:
        print('OK')
    else:
        print("Некорректный адрес")
