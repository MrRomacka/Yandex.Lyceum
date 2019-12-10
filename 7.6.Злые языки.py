a = int(input())
b = int(input())
c = int(input())

eng = set()
deu = set()
fra = set()

for i in range(a):
    eng.add(input())

for j in range(b):
    deu.add(input())

for k in range (c):
    fra.add(input())

ab = set(eng & deu)
bc = set(deu & fra)
ac = set(eng & fra)
abc = set(eng & deu & fra)
doub = set((ab | ac | bc) ^ abc)

if len(doub) == 0:
    print('NO')
else:
    print(len(doub))