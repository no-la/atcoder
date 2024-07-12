N, M, X, Y = map(int, input().split())
from collections import defaultdict
d = defaultdict(list)
for _ in range(M):
    a, b, t, k = map(int, input().split())
    a -= 1
    b -= 1
    d[a].append((b, t, k))
    d[b].append((a, t, k))

import heapq

def dijkstra(edges, N, start=0):
    """
    parameter
        edges[i][_] : [点iから向かう点, コスト]
        N : 点の個数(=len(edges))
        start : 探索を始める点
    """
    dist = [float("inf")]*N # dist[i]: startからiまでのコスト
    dist[start] = 0 # スタートは0
    seen = [False]*N
    
    hq = [] # コスト, 向かう点
    heapq.heappush(hq, (0, start))

    while hq:
        _, current = heapq.heappop(hq)
        
        if seen[current]: # 同じ点を二度見ない
            continue
        seen[current] = True
        for to, t, k in edges[current]:
            ndist = -(-dist[current]//k)*k + t
            if ndist < dist[to]: # 最短距離を更新できるときだけheappush()
                dist[to] = ndist
                heapq.heappush(hq, (ndist, to))
    return dist

ans = dijkstra(d, N, X-1)[Y-1]
print(ans if ans!=float("inf") else -1)
