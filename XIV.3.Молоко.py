NumberOfBottles = int(input())
List = [int(input()) for i in range(NumberOfBottles)]
a, b = int(input()), int(input())
for x in List:
    if a <= x <= b:
        print(x)