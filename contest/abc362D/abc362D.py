N, M = map(int, input().split())
A = list(map(int, input().split()))
from collections import defaultdict
d = defaultdict(list)
for _ in range(M):
    u, v, b = map(int, input().split())
    u -= 1
    v -= 1
    d[u].append([v, b])
    d[v].append([u, b])


import heapq

def dijkstra(edges, N, start=0):
    """
    parameter
        edges[i][_] : [点iから向かう点, コスト]
        N : 点の個数(=len(edges))
        start : 探索を始める点
    """
    dist = [float("inf")]*N # dist[i]: startからiまでのコスト
    dist[start] = A[start]
    seen = [False]*N
    
    hq = [] # コスト, 向かう点
    heapq.heappush(hq, (0, start))

    while hq:
        _, current = heapq.heappop(hq)
        
        if seen[current]: # 同じ点を二度見ない
            continue
        seen[current] = True
        for to, cost in edges[current]:
            ndist = dist[current] + cost + A[to]
            if ndist < dist[to]: # 最短距離を更新できるときだけheappush()
                dist[to] = ndist
                heapq.heappush(hq, (dist[to], to))
    return dist

ans = dijkstra(d, N)
print(*ans[1:])
