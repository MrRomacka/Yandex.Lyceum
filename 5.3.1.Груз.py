n = int(input())
way = 0
height = 0
for i in range(n):
    ton = int(input())
    for j in range(ton):
        h = int(input())
        if j == 0:
            min_ton = h
        elif h < min_ton:
            min_ton = h
    if height < min_ton:
        height = min_ton
        way = i + 1
print(way, height)