N = int(input())
ListOfIntegers = []
answer = 0
for i in range(N):
    ListOfIntegers.append(int(input()))
Number = int(input())
for j in range(len(ListOfIntegers)):
    for k in range(j + 1, len(ListOfIntegers)):
        if Number == ListOfIntegers[j] * ListOfIntegers[k]:
            answer = True
            break
        if answer:
            break
if answer:
    print('Да')
else:
    print('Нет')
