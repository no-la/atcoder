N = int(input())
d = [[] for _ in range(N)]
deg = [0] * N
for _ in range(N - 1):
    u, v = map(lambda x: int(x) - 1, input().split())
    d[u].append(v)
    d[v].append(u)
    deg[u] += 1
    deg[v] += 1

# degを見て、
# 2-3-3-3-3-...-3-2
# になっているパスの組み合わせを数えればいい

start = []
for i in range(N):
    if deg[i] == 3:
        start.append(i)

# DFS
from collections import deque

ans = 0
seen = [False] * N
for s in start:
    if seen[s]:
        continue
    seen[s] = True
    todo = deque([s])
    leaf = set()
    while todo:
        v = todo.pop()
        for w in d[v]:
            if seen[w]:
                continue
            if deg[w] == 2:
                leaf.add(w)
            elif deg[w] == 3:
                todo.append(w)
                seen[w] = True

    ans += len(leaf) * (len(leaf) - 1) // 2

print(ans)
