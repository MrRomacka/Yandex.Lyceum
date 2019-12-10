string = input()
NumberOfLetter = int(input())
if len(string) < NumberOfLetter:
    print("ОШИБКА")
else:
    RealNumber = NumberOfLetter - 1
    LovelyLetter = input()
    if len(LovelyLetter) != 1:
        print('ОШИБКА')
    elif LovelyLetter == string[RealNumber]:
        print('ДА')
    else:
        print('НЕТ')