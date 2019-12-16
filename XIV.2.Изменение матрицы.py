NumberOne = int(input())
NumberTwo = int(input())
matrix = []
for i in range(NumberOne):
    matrix.append([])
    for j in range(NumberTwo):
        st = input()
        matrix[i].append(st)
print(matrix)

for i in range(NumberOne):
    for j in range(NumberTwo):
        print(matrix[i][j], end=' ')
    print()

for j in range(NumberTwo):
    for i in range(NumberOne):
        print(matrix[i][j], end=' ')
    print()
