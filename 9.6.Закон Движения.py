# r (t+dt) = r(t) + v(t)dt + a(t)*(dt**2)/2
# f = mg - kV

x = float(input('X0 = '))
y = float(input('Y0 = '))
vx = float(input('V0x = '))
vy = float(input('V0y = '))
m = float(input('M = '))
dt = float(input('dT = '))
T = float(input('T = '))
g = 10
ExtraT = 0
a = -10

while ExtraT < T:
    ExtraT += dt
    y = y + vy * dt + a * (dt ** 2) / 2
    x = x + vx * dt
    vy = vy + a * dt
    if (y < 0) or (x < 0):
        print('X или Y отрицательно')
        break
    print(f"T = {ExtraT}, x({ExtraT}) = {x}, y({ExtraT}) = {y}, Vy({ExtraT}) = {vy}")