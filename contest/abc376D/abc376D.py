N, M = map(int, input().split())
INF = 10**10
d = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    d[a].append(b)
    d[b].append(a)

import heapq


def dijkstra(edges, N, start=0):
    """
    parameter
        edges[i][_] : [点iから向かう点, コスト]
        N : 点の個数(=len(edges))
        start : 探索を始める点
    """
    dist = [float("inf")] * N  # dist[i]: startからiまでのコスト
    dist[start] = 0  # スタートは0
    seen = [False] * N

    hq = []  # コスト, 向かう点
    heapq.heappush(hq, (0, start))

    while hq:
        _, current = heapq.heappop(hq)

        if seen[current]:  # 同じ点を二度見ない
            continue
        seen[current] = True
        for to in edges[current]:
            cost = 1
            if (
                dist[current] + cost < dist[to]
            ):  # 最短距離を更新できるときだけheappush()
                dist[to] = dist[current] + cost
                heapq.heappush(hq, (dist[current] + cost, to))
    return dist


dist = dijkstra(d, N)
# print(dist)

# DFS
from collections import deque

ans = INF

todo = deque([0])
seen = [0] * N  # ここはsetでもよい
seen[todo[0]] = 1
while todo:
    v = todo.pop()
    for w in d[v]:
        if seen[w] < 2:
            continue
        todo.append(w)
        seen[w] += 1
        if dist[v] + 1 != dist[w]:
            ans = min(ans, dist[v] + 1 + dist[w])

print(ans if ans < INF else -1)
