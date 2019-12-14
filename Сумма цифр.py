n = int(input())
s = 0

for elem in str(n):
    s += int(elem)

print(s)
s = 0

st = str(n)
for i in range(len(st)):
    s += int(st[i])

print(s)
s = 0

while n != 0:
    s += n % 10
    n //= 10

print(s)