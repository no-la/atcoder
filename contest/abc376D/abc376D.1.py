N, M = map(int, input().split())
INF = 10**10
d = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    d[a].append(b)

# BFS
from collections import deque

ans = INF

todo = deque([[0, 0]])
dist = [-1] * N  # todo[0]からの距離のリスト
dist[0] = 0
while todo:
    u, v = todo.popleft()
    for w in d[v]:
        if dist[w] != -1:  # 既に調べた点は飛ばす
            if w != u:
                ans = min(ans, dist[v] + 1 + dist[w])
                # print(v, w, dist)
            continue
        todo.append([v, w])
        dist[w] = dist[v] + 1

print(ans if ans < INF else -1)
