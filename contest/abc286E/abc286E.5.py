import heapq

INF = 10**10


def dijkstra(edges, N, start=0):
    """
    parameter
        edges[i][_] : [点iから向かう点, コスト]
        N : 点の個数(=len(edges))
        start : 探索を始める点
    """
    dist = [(INF, -INF) for _ in range(N)]
    dist[start] = (0, -A[start])
    seen = [False] * N

    hq = []  # コスト, 向かう点
    heapq.heappush(hq, ((0, -INF), start))

    while hq:
        _, current = heapq.heappop(hq)

        if seen[current]:  # 同じ点を二度見ない
            continue
        seen[current] = True
        for to, cost in edges[current]:
            ndist = (dist[current][0] + cost[0], dist[current][1] + cost[1])
            if ndist < dist[to]:  # 最短距離を更新できるときだけheappush()
                dist[to] = ndist
                heapq.heappush(hq, (dist[to], to))
    return dist


N = int(input())
A = list(map(int, input().split()))
S = [input() for _ in range(N)]
Q = int(input())

E = [[(j, (1, -A[j])) for j in range(N) if S[i][j] == "Y"] for i in range(N)]

dist = [None] * N
for i in range(N):
    dist[i] = dijkstra(edges=E, N=N, start=i)
for _ in range(Q):
    u, v = map(lambda x: int(x) - 1, input().split())

    ans = (dist[u][v][0], -dist[u][v][1])
    if ans[0] == INF:
        print("Impossible")
    else:
        print(*ans)
