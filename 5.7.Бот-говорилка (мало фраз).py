a = str(input("Здравствуй, это Бот-Говорилка. Напиши мне что-нибудь, и я отвечу.",
              "Как только захочешь остановиться, напиши Стоп"))

while True:
    print()
    if a == "Стоп":
        break
    elif "привет" in a or 'Привет' in a:
        print('Приветствую тебя, пользователь.')
    elif "как дела" in a or "Как дела" in a:
        print('Как обычно. Всё прекрасно.')
        print('А у тебя?')
    elif "хорошо" in a or "Хорошо" in a or "Замечательно" in a or "Прекрасно" in a or "Отлично" in a:
        print('Это прекрасно.')

    else:
        print("Я ничего не понял, попробуй перефразировать.")