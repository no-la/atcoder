"""AC解"""

N, W = map(int, input().split())
M = N * (10**3)

dp = [[W + 1] * (M + 1) for _ in range(N + 1)]
dp[0][0] = 0
# dp[i][j]: i個目まで見て価値の総和がjのときの重さの総和の最小値

for i in range(N):
    w, v = map(int, input().split())
    for j in range(M + 1):
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
        if dp[i][j] + w <= W:
            dp[i + 1][j + v] = min(dp[i + 1][j + v], dp[i][j] + w)


print(max([j for j in range(M + 1) if dp[N][j] <= W]))
