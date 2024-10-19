N, M = map(int, input().split())
INF = 10**10
d = [[] for _ in range(N)]
e = [[] for _ in range(N)]
EDGES = []
for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    d[a].append(b)
    e[b].append(a)
    EDGES.append([a, b])

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


to = dijkstra(d, N)
from_ = dijkstra(e, N)
# print(dist)

ans = INF
for a, b in EDGES:
    ans = min(ans, to[a] + from_[b] + 1)

print(ans if ans < INF else -1)
