N, M, K = map(int, input().split())
d = [[] for _ in range(N)]
e = []
for i in range(M):
    u, v, a = map(int, input().split())
    u -= 1
    v -= 1
    d[u].append((v, i))
    d[v].append((u, i))
    e.append(a)
s = [False] * N
for x in list(map(int, input().split())):
    s[x - 1] = True

# BFS
from collections import deque

todo = deque([(0, 1)])  # 頂点, 状態
dist = [[-1] * N for _ in range(2)]
dist[1][0] = 0
while todo:
    v, vs = todo.popleft()
    if s[v]:
        dist[vs ^ 1][v] = dist[vs][v]
    # print(v, dist)
    for ws in range(2):
        if ws != vs and not s[v]:
            continue
        for w, ei in d[v]:
            if dist[ws][w] != -1:  # 既に調べた点は飛ばす
                continue
            if e[ei] == ws:
                todo.append((w, ws))
                dist[ws][w] = dist[vs][v] + 1

    if dist[0][N - 1] > 0 or dist[1][N - 1] > 0:
        break

ans = dist[0][N - 1]
if ans == -1:
    ans = dist[1][N - 1]
else:
    ans = min(ans, dist[1][N - 1])
print(ans)
# print(*dist, sep="\n")
