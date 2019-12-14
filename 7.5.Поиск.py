N = int(input())
lst = list()
for i in range(N):
    data = input()
    lst.append(data)

search = input()
for elem in lst:
    if search in elem:
        print(elem)