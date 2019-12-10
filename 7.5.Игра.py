perviylist = set()
vtoroylist = set()

a = input()
while a != "":
    perviylist.add(a)
    a = input()

b = input()
while b != "":
    vtoroylist.add(b)
    b = input()

c = set(perviylist & vtoroylist)
dl = len(c)

if dl == 0:
    print('Empty')
else:
    for i in range(dl):
        print(c)
