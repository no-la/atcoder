import sys

input = lambda: sys.stdin.readline().rstrip()
N, M, Q = map(int, input().split())

d = [set() for _ in range(M)]
every = [False] * N

for _ in range(Q):
    t, *others = map(int, input().split())
    if t == 1:
        x, y = others
        d[y - 1].add(x - 1)
    elif t == 2:
        x = others[0]
        every[x - 1] = True
    else:
        x, y = others
        if every[x - 1] or x - 1 in d[y - 1]:
            print("Yes")
        else:
            print("No")
