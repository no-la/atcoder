N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
K = max([*A, *B]) + 1
INF = 2 * (10**5) + 1

d = [INF] * K
# d[i]: はじめてA[j]<=iとなるj

for j in range(N):
    if d[A[j]] == INF:
        d[A[j]] = j

for i in range(K - 1):
    d[i + 1] = min(d[i + 1], d[i])

# print(d)
for i in range(M):
    print(d[B[i]] + 1 if d[B[i]] < INF else -1)
