x = 0
v = 0
a = 3
dt = 0.05
T = 0
m = 2
g = 10
k = 0.3
print(f'x({T})={x}\nv({T})={v}\n')
with open('out1.txt', 'w') as outf:
    while T <= 1.5:
        print(f'{T}\t{x}', file=outf)
        f = m * g - k * v
        a = f / m
        x = x + v * dt + a * (dt ** 2) / 2
        v = v + a * dt
        T += dt
        print(f'x({T})={x}\nv({T})={v}')

 print(f'{T}\t{x}', file=outf)