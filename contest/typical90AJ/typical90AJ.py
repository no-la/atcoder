import sys

input = lambda: sys.stdin.readline().rstrip()
N, Q = map(int, input().split())
d1 = []
d2 = []
P = []
for _ in range(N):
    x, y = map(int, input().split())
    d1.append(x + y)
    d2.append(x - y)
    P.append((x, y))

d = [max(d1), min(d1), max(d2), min(d2)]
for _ in range(Q):
    x, y = P[int(input()) - 1]
    print(max(d[0] - (x + y), -d[1] + (x + y), d[2] - (x - y), -d[3] + (x - y)))
