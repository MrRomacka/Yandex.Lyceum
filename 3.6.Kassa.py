item = float(input("Введите стоимость товара"))
count = 0
while item >= 0:
    if item >=1000:
        item = item * 0.95
    else:
        pass
    count = count + item
    item = float(input("Введите стоимость следующего товара"))

print(count)
