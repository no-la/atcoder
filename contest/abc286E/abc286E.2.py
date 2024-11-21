N = int(input())
A = list(map(int, input().split()))
S = [input() for _ in range(N)]
Q = int(input())
INF = 100000000

import heapq


def dijkstra(N, start, goal):
    """
    parameter
        N : 点の個数(=len(edges))
        start : 探索を始める点
    """
    dist = [INF] * N  # dist[i]: startからiまでのコスト
    dist[start] = 0  # スタートは0
    value = [0] * N
    value[start] = -A[start]
    seen = [False] * N

    hq = []  # コスト, 向かう点
    heapq.heappush(hq, ((0, -A[start]), start))

    while hq:
        _, current = heapq.heappop(hq)

        if seen[current]:  # 同じ点を二度見ない
            continue
        seen[current] = True
        for to in range(N):
            if S[current][to] == "N":
                continue
            cost = (dist[to], value[to])
            ncost = (dist[current] + 1, value[current] - A[to])
            # print(current, "->", to, cost, ncost)
            if ncost < cost:  # 最短距離を更新できるときだけheappush()
                dist[to] = ncost[0]
                value[to] = ncost[1]
                heapq.heappush(hq, (cost, to))
    # print(start, goal, dist, value)
    return dist[goal], -value[goal]


for _ in range(Q):
    u, v = map(int, input().split())
    ans = dijkstra(N, u - 1, v - 1)
    print(*ans if ans[0] != INF else ("Impossible",))
