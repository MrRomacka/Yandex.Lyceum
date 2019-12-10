d = int(input("Число: "))
m = int(input("Месяц: "))
year = str(input("Год: "))
y = int(year[2:4])
c = int(year[0:2])

week = d + ((13 * m - 1) // 5) + y + (y // 4 + c // 4 - 2 * c + 777)
print(week)
day = week % 7
if day == 1:
    print("Понедельник")
elif day == 2:
    print("Вторник")
elif day == 3:
    print("Среда")
elif day == 4:
    print("Четверг")
elif day == 5:
    print("Пятница")
elif day == 6:
    print("Суббота")
elif day == 7:
    print("Воскресенье")
