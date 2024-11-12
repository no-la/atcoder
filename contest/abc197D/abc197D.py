N = int(input())
sx, sy = map(int, input().split())
gx, gy = map(int, input().split())

from math import sin, cos, pi

s = sx + sy * 1j
g = gx + gy * 1j
c = (s + g) / 2

theta = 2 * pi / N
ans = (s - c) * (cos(theta) + sin(theta) * 1j) + c


def f(t):
    return f"{t:.11f}"


# print(ans.real, ans.imag)
print(f(ans.real), f(ans.imag))
