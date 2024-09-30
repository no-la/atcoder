"""AC"""

from collections import defaultdict

N, M = map(int, input().split())
INF = 10**10
dist = [[INF] * N for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    dist[a][b] = c

for i in range(N):
    dist[i][i] = 0

ans = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    ans += sum([sum([v if v < INF else 0 for v in l]) for l in dist])

print(ans)
