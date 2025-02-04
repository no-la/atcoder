import sys
import math

input = lambda: sys.stdin.readline().rstrip()
T = int(input())
L, X, Y = map(int, input().split())
r = L / 2
Q = int(input())
for _ in range(Q):
    E = int(input())
    theta = math.pi + E * 2 * math.pi / T
    x = math.sqrt(X**2 + (Y - r * math.sin(theta)) ** 2)
    y = r + r * math.cos(theta)

    ans = math.atan(y / x) * 180 / math.pi
    print(ans)
