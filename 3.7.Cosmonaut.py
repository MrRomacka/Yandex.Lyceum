rost = input()
minr = 300
maxr = 0
kolvo = 0

while rost != "!":
    rost = int(rost)
    if rost > 190 or rost < 150:
        pass
    else:
        kolvo = kolvo + 1
        if minr > rost:
            minr = rost
        else:
            pass
        if maxr < rost:
            maxr = rost
        else:
            pass
    rost = input()

print(kolvo)
print(maxr)
print(minr)