N, M, K = map(int, input().split())
D = []
for _ in range(M):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    D.append((a, b, c))
E = list(map(lambda x: int(x) - 1, input().split()))

# 最新の状態だけもちつつDPする感じ
INF = 10**16
cost = [INF] * N
cost[0] = 0
for i in E:
    a, b, c = D[i]
    if cost[a] == INF:
        continue
    cost[b] = min(cost[b], cost[a] + c)

print(cost[N - 1] if cost[N - 1] < INF else -1)
