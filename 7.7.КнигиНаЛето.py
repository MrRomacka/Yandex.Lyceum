N = int(input())
M = int(input())

homelib = set()

for i in range(N):
    homelib.add(input())

for j in range(M):
    kniga = str(input())
    if kniga in homelib:
        print("YES")
    else:
        print("NO")