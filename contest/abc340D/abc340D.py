import heapq
def dijkstra(edges, N, start=0):
    """
    parameter
        edges[i][_] : [点iから向かう点, コスト]
        N : 点の個数
        start : 探索を始める点
    """
    dist = [float("inf")]*N
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
    return dist


N = int(input())
A = [[] for _ in range(N)] # A[i][_]: [ステージiから向かうステージ, コスト]

for i in range(N-1):
    a, b, x = map(int, input().split())
    A[i].append((i+1, a))
    A[i].append((x-1, b)) #0-indexed

dist = dijkstra(A, N)
print(dist[N-1])
