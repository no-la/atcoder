N = int(input())
P = list(map(float, input().split()))

dp = [[0] * (N + 1) for _ in range(N + 1)]
# dp[i][j]: P[:i]まで見て表がj枚である確率
dp[0][0] = 1

for i in range(N):
    for j in range(N + 1):
        if j + 1 < N + 1:
            dp[i + 1][j + 1] += dp[i][j] * P[i]
        dp[i + 1][j] += dp[i][j] * (1 - P[i])

print(sum(dp[N][(N // 2) + 1 :]))
# print(*dp, sep="\n")
