N, M, _X = map(int, input().split())
d = [[] for _ in range(N)]
E = [None]*M
for i in range(M):
    a, b, s, t = map(int, input().split())
    a -= 1
    b -= 1
    d[a].append((s, t, b, i))
    E[i] = [a, b, s, t]

X = [0]*M
X[0] = _X

for l in d:
    l.sort()


import bisect
# DFS
from collections import deque
todo = deque([0])
# seen = [False]*N # ここはsetでもよい
# seen[todo[0]] = True
while todo:
    i = todo.pop()
    a, b, s, t = E[i]
    k = bisect.bisect_left(d[b], (t, 0, 0, 0))
    for ns, nt, c, ni in d[b][k:]:
        if X[ni]<t+X[i]-ns:
            X[ni] = t+X[i]-ns
            todo.append(ni)

print(*X[1:])
