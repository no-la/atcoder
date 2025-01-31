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


N, M = map(int, input().split())
edges = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append((b, c))
    edges[b].append((a, c))

dist_from_1 = dijkstra(edges=edges, N=N, start=0)
dist_from_N = dijkstra(edges=edges, N=N, start=N - 1)

for k in range(N):
    print(dist_from_1[k] + dist_from_N[k])
