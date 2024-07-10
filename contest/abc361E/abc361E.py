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
        for to, cost in edges[current]:
            if dist[current] + cost < dist[to]: # 最短距離を更新できるときだけheappush()
                dist[to] = dist[current] + cost
                heapq.heappush(hq, (dist[current] + cost, to))
    # print(dist)
    return max([(dist[i], i) for i in range(N) if i!=start])

N = int(input())
d = [[] for _ in range(N)]
S = 0
for _ in range(N-1):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    d[a].append((b, c))
    d[b].append((a, c))
    S += c


_, u = dijkstra(d, N)
cost, v = dijkstra(d, N, u)
# print(u, v, cost)
print(cost + (S-cost)*2)
