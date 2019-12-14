ListOfMoney = input()
Currency = ''
for i in range(len(ListOfMoney)):
    if (ListOfMoney[i] != ',') and (ListOfMoney[i] != ';'):
        Currency += ListOfMoney[i]
    elif ListOfMoney[i] == ',':
        Final = int(Currency)
        if Final >= 1000000000:
            print(Final, end=',')
        Currency = ''
    elif ListOfMoney[i] == ';':
        Final = int(Currency)
        if Final >= 1000000000:
            print(Final)
        print()
        Currency = ''