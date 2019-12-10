path = int(input())
sms = input()
f = ''

for i in range(len(sms)):
    order = ord(sms[i])
    if order > 1103 or order < 1040:
        order = order
    elif order < 1072:
        order += path
        if order > 1071:
            order -= 32
    else:
        order += path
        if order > 1103:
            order -= 32
    f += chr(order)

print(f)


