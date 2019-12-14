a1 = 1
a2 = 1
n = 10**1000
print(a1)
print(a2)
while a2<n:
    a1, a2 = a2, a1 + a2
    print (a2)