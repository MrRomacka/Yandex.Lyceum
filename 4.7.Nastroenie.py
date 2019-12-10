nas=input('Какое у Вас настроение?')

if "не" in nas:
    print('Ладно. Удачи сегодня.')
elif "хорош" in nas or "прекрасн" in nas or "отличн" in nas:
    print("Превосходно, у меня тоже)")
elif "плох" in nas or "ужас" in nas:
    print('Ничего страшного, всё наладится.')
else:
    print("Ладно, будьте здоровы.")