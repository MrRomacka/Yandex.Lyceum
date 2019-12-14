n = int(input())
lst = list()
for _ in range(n):
    num = int(input())
    lst.append(num)
for i in range(len(lst) - 1):
    print(lst[i] + lst[i + 1])