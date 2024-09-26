H, W = map(int, input().split())
A = [input() for _ in range(H)]
MOD = 10**9 + 7

dp = [[0] * W for _ in range(H)]
dp[0][0] = 1

for i in range(H):
    for j in range(W):
        if i == H and j == W:
            continue
        if A[i][j] == "#":
            dp[i][j] = 0
            continue
        if i + 1 < H:
            dp[i + 1][j] += dp[i][j]
            dp[i + 1][j] %= MOD
        if j + 1 < W:
            dp[i][j + 1] += dp[i][j]
            dp[i][j + 1] %= MOD

print(dp[H - 1][W - 1])
