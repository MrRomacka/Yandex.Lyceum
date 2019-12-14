N = int(input())
count = 1
ii = 1
while count <= N:
    for i in range (ii):
        print(count, end=" ")
        count += 1
        if count > N:
            break
    print()
    ii += 1