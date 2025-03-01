import sys

input = lambda: sys.stdin.readline().rstrip()


import heapq


def dijkstra(edges, N, start=0):
    """
    parameter
        edges[i][_] : [点iから向かう点, コスト]
        N : 点の個数(=len(edges))
        start : 探索を始める点
    """
    dist = [[float("inf")] * 2 for _ in range(N)]
    dist[start][0] = 0  # スタートは0
    seen = [[False] * 2 for _ in range(N)]

    # 点は (i, 裏表) とする
    hq = []  # コスト, 向かう点
    heapq.heappush(hq, (0, start, 0))

    while hq:
        _, current, r = heapq.heappop(hq)

        if seen[current][r]:  # 同じ点を二度見ない
            continue
        seen[current][r] = True
        for to, cost in edges[current][r]:
            if (
                dist[current][r] + cost < dist[to][r]
            ):  # 最短距離を更新できるときだけheappush()
                dist[to][r] = dist[current][r] + cost
                heapq.heappush(hq, (dist[to][r], to, r))

        # 反転
        nr = r ^ 1
        cost = X
        if (
            dist[current][r] + cost < dist[current][nr]
        ):  # 最短距離を更新できるときだけheappush()
            dist[current][nr] = dist[current][r] + cost
            heapq.heappush(hq, (dist[current][nr], current, nr))

    return dist


# 工夫してダイクストラ
N, M, X = map(int, input().split())

edges = [[[] for _ in range(2)] for _ in range(N)]
for _ in range(M):
    u, v = map(lambda x: int(x) - 1, input().split())
    edges[u][0].append((v, 1))
    edges[v][1].append((u, 1))

dist = dijkstra(edges, N)
print(min(dist[N - 1]))
