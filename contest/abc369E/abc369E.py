N, M = map(int, input().split())
INF = 10**15
dist = [[INF]*N for _ in range(N)]
for i in range(N):
    dist[i][i] = 0
# dist[i][j]: 島iから島jへの最短コスト
E = [None]*M
for i in range(M):
    u, v, t = map(int, input().split())
    u -= 1
    v -= 1
    if dist[u][v]>t:
        dist[u][v] = t
        dist[v][u] = t
    E[i] = (u, v, t)
Q = int(input())

# ワーシャルフロイド法
for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

# print(*dist, sep="\n")

import itertools
for _ in range(Q):
    K = int(input())
    B = list(map(lambda x: int(x)-1, input().split()))
    ans = INF
    # 順列 O(nPk)<=n!
    for l in itertools.permutations(B, K):
        for i in range(2 ** K):
            cost = 0
            before = 0
            for j in range(K):
                u, v, t = E[l[j]]
                if (i >> j) & 1:
                    u, v = v, u
                # print(before, "->", u)
                cost += dist[before][u] + t
                before = v
            cost += dist[before][N-1]
            # print("-"*20, cost, sep="\n")
            ans = min(ans, cost)
        
    print(ans)
