import sys

input = lambda: sys.stdin.readline().rstrip()
N, Q = map(int, input().split())

pc = [[] for _ in range(N)]
server = ""

for _ in range(Q):
    t, *others = input().split()
    t = int(t)
    if t == 1:
        p = int(others[0])
        pc[p - 1] = [server]
    elif t == 2:
        p, s = others
        p = int(p)
        pc[p - 1].append(s)
    elif t == 3:
        p = int(others[0])
        server = "".join(pc[p - 1])

print(server)
