N, M, _X = map(int, input().split())
d = [[] for _ in range(N)]
for _ in range(M):
    a, b, s, t = map(int, input().split())
    a -= 1
    b -= 1
    d[a].append((s, t, b))

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
    a = todo.pop()
    for s, t, b in d[a]:
        k = bisect.bisect_left(d[b], (t+X[a], 0, 0))
        if not k<len(d[b]):
            X[b] = max(X[b], 0)
        else:
            X[b] = max(X[b], t+X[a]-d[b][k][0])

print(*X[1:])
