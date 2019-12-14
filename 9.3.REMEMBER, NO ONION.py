N = int(input())
receipts = []

for i in range(N):
    st = input()
    if 'лук' in st:
        continue
    receipts.append(st)

print(', '.join(receipts))