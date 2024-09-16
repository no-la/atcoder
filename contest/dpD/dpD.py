N, W = map(int, input().split())

dp = [[0] * (W + 1) for _ in range(N + 1)]
# dp[i][j]: i個目まで見て重さjのときの勝ちの最大値

for i in range(N):
    w, v = map(int, input().split())
    for j in range(W):
        ni = i + 1
        dp[ni][j] = max(dp[ni][j], dp[i][j])

        nj = j + w
        if nj <= W:
            dp[ni][nj] = max(dp[ni][nj], dp[i][j] + v)

print(max(dp[N]))
