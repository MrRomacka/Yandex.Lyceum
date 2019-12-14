skor = int(input("Введите скорость землекопа: "))
dlin = int(input("Введите длину рва: "))
kolvodney = int(input("Введите количество дней: "))

if skor == 0 or kolvodney == 0:
    print ('Ты кокер?')
else:
    if dlin % (skor * kolvodney) == 0:
        zeml = dlin / (skor * kolvodney)
    else:
        zeml = dlin // (skor * kolvodney) + 1
    print('Количество нужных землекопов:', zeml)
