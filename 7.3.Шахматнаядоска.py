letters = 'ABCDEFGH'
n = int(input())
for i in reversed(range(1, n+1)):
    for let in letters[:n]:
        print(f"{let}{i}", end=" ")
    print()

