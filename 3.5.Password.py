password = input("Введите пароль: ")
password2 = input('Повторите пароль: ')

while len(password)<8 or password != password2:
    if len(password)<8:
        print("Пароль слишком короткий.")
    elif password != password2:
        print("Пароли различаются.")
    else:
        break
    print('Ошибка. Введите снова.')
    password = input()
    password2 = input()

print("Пароль подходящий.")