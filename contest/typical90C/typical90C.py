N = int(input())
d = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    d[a].append(b)
    d[b].append(a)

# 木の直径 + 1
# が答え

# BFS
from collections import deque

todo = deque([0])
dist_from_0 = [-1] * N
dist_from_0[todo[0]] = 0
while todo:
    v = todo.popleft()
    for w in d[v]:
        if dist_from_0[w] != -1:  # 既に調べた点は飛ばす
            continue
        todo.append(w)
        dist_from_0[w] = dist_from_0[v] + 1

u = max([(v, i) for i, v in enumerate(dist_from_0)])[1]

todo = deque([u])
dist_from_u = [-1] * N
dist_from_u[todo[0]] = 0
while todo:
    v = todo.popleft()
    for w in d[v]:
        if dist_from_u[w] != -1:  # 既に調べた点は飛ばす
            continue
        todo.append(w)
        dist_from_u[w] = dist_from_u[v] + 1

ans = max(dist_from_u) + 1
print(ans)
