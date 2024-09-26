H, W = map(int, input().split())
A = [input() for _ in range(H)]
MOD = 10**9 + 7

dp = [[0] * W for _ in range(H)]
dp[0][0] = 1

for i in range(H):
    for j in range(W):
        if i == 0 and j == 0:
            continue
        if A[i][j] == "#":
            dp[i][j] = 0
            continue
        if i > 0:
            dp[i][j] += dp[i - 1][j]
            dp[i][j] %= MOD
        if j > 0:
            dp[i][j] += dp[i][j - 1]
            dp[i][j] %= MOD

print(dp[H - 1][W - 1])
