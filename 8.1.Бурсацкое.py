number = int(input())
while number < 1000000000:
    numst = str(number)
    firstofnu = int(numst[0])
    if firstofnu == 1:
        break
    else:
        number = number * firstofnu

print(number)