N, M = map(int, input().split())
H = list(map(int, input().split()))

# 降って増える楽しさは H[0]-H[i] で大体出せる
# 登って減る楽しさを正のコストとしてdijkstra


def f(x, y):
    return 0 if x - y >= 0 else y - x


d = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(lambda x: int(x) - 1, input().split())
    d[u].append([v, f(H[u], H[v])])
    d[v].append([u, f(H[v], H[u])])


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
        for to, cost in edges[current]:
            if (
                dist[current] + cost < dist[to]
            ):  # 最短距離を更新できるときだけheappush()
                dist[to] = dist[current] + cost
                heapq.heappush(hq, (dist[current] + cost, to))
    return dist


v = dijkstra(d, N)
ans = 0
for i in range(N):
    ans = max(ans, H[0] - H[i] - v[i])

print(ans)
# print(v)
