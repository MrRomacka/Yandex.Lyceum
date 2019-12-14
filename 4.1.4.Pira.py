n = int(input())
space = str(input())
sym = str(input())

for i in range(n):
    print(space * (n - i - 1) + sym * (2 * i + 1) + space * (n - i - 1))