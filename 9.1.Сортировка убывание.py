N = int(input())
BeginPos = []
EndPos = []

for i in range(N):
    BeginPos.append(int(input()))

BeginPos = sorted(BeginPos)

for j in range(N):
    EndPos.append(str(BeginPos[N - j - 1]))

print('\n'.join(EndPos))