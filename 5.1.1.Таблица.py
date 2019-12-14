N = int(input())
F = int(input())
if N > F:
    N, F = F, N
for i in range (N, F + 1):
    for j in range(N, F + 1):
        print(f'{i * j}\t', end='')
    print()