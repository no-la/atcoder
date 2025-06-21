import sys

input = lambda: sys.stdin.readline().rstrip()
N, Q = map(int, input().split())

query = [input().split() for _ in range(Q)]

server = -1  # server依存しているpc
ans = []
for t, *others in query[::-1]:
    t = int(t)
    if t == 1:
        # p -> server'
        p = int(others[0])
        if p != server:
            continue
        server = -1
    elif t == 2:
        p, s = others
        p = int(p)
        if p != server:
            continue
        ans.append(s)
    elif t == 3:
        if server != -1:
            continue
        # server -> p
        p = int(others[0])
        server = p

print("".join(ans[::-1]))
