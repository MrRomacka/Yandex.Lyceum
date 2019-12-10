a = 100000000000
b = int(input())
kup = 0
prod = 0

while a > b:
    a = b
    b = int(input())

kup = b

while a < b:
    a = b
    b = int(input())

prod = b

while b != 0:
    b = int(input())

razn = prod - kup

print(kup, prod, razn)