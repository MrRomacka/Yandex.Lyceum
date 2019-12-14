N = int(input())
LetTheGamePlay = []

for i in range(N):
    LetTheGamePlay.append(input())

K = int(input())

for j in range(K):

    Quantity = int(input())
    EndOfRound = [''] * Quantity
    for k in range(Quantity):
        EndOfRound[int(input()) - 1] = LetTheGamePlay[k]
    LetTheGamePlay = EndOfRound


print('\n'.join(LetTheGamePlay))