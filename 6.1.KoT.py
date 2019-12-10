stra = str(print())
counter = 0
kotokount = -1
kountfor = 0

while stra != "СТОП":
    kountfor = kountfor + 1
    if "кот" in stra:
        counter = counter + 1
        if kotokount <= 0:
            kotokount = kountfor
    str = print()

print (counter, kotokount)