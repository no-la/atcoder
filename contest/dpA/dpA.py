N = int(input())
H = list(map(int, input().split()))
INF = 10**10

dp = [INF] * N
dp[0] = 0
# dp[i]: 足場iに辿り着くためのコストの最小値

# 配るdp
for i in range(N - 1):
    for j in range(i + 1, min(N, i + 3)):
        dp[j] = min(dp[j], dp[i] + abs(H[i] - H[j]))

print(dp[N - 1])
