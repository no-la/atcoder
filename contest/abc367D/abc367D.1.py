N, M = map(int, input().split())
A = list(map(int, input().split()))

A = A + A
d = [0] * M
# d[i:] 対象区間にある i mod M の個数
dist = [0] * (2 * N)
# dist[i]: 0からiまでの距離

# init
for i in range(1, 2 * N):
    dist[i] = dist[i - 1] + A[i - 1]
for i in range(N):
    d[dist[i] % M] += 1

# main
ans = 0
for i in range(N):
    d[dist[i] % M] -= 1
    ans += d[dist[i] % M]
    d[dist[i + N] % M] += 1

print(ans)
