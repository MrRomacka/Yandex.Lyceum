# r (t+dt) = r(t) + v(t)dt + a(t)*(dt**2)/2
# f = mg - kV

x = float(input('X0 = '))
y = float(input('Y0 = '))
vx = float(input('V0x = '))
vy = float(input('V0y'))
m = float(input('M = '))
dt = float(input('dT = '))
T = float(input('T = '))
k = float(input('K = '))
g = 10
ExtraT = 0

while ExtraT < T:
    ExtraT += dt
    ay = (m * g - k * vy) / m
    ax = (-k * vx) / m
    y = y + vy * dt + ay * (dt ** 2) / 2
    x = x + vx * dt
    vx = vx + ax * dt
    vy = vy + ay * dt
    if (y < 0) or (x < 0):
        print('X или Y отрицательно')
        break
    print(f"T = {ExtraT}, x({ExtraT}) = {x}, y({ExtraT}) = {y}, Vy({ExtraT}) = {vy}, Vx({ExtraT}) = {vx}")