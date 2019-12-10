N = int(input())
lst = []
k = 0

for i in range(2,N):
    for j in range(2,i):
        if i % j == 0:
            k = k + 1
    if k == 0:
        lst.append(i)
        print(i)
    else:
        k = 0
