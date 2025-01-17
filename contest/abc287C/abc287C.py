# 葉を1つ見つければいい

N, M = map(int, input().split())
d = [[] for _ in range(N)]
deg = [0] * N
for _ in range(M):
    u, v = map(lambda x: int(x) - 1, input().split())
    d[u].append(v)
    d[v].append(u)
    deg[u] += 1
    deg[v] += 1

leafs = [i for i in range(N) if deg[i] == 1]

if len(leafs) != 2 or M != N - 1:
    print("No")
    exit()

# あとは連結だけかな
# DFS
from collections import deque

todo = deque([0])
seen = [False] * N
seen[0] = True
while todo:
    v = todo.pop()
    for w in d[v]:
        if seen[w]:
            continue
        todo.append(w)
        seen[w] = True

if all(seen):
    print("Yes")
else:
    print("No")
