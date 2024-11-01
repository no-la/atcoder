N, K = map(int, input().split())
A = list(map(int, input().split()))

# 最大Nターン
dp = [[0] * (N + 1) for _ in range(2)]
# dp[i][j]: iの手番の直後で山がjのときのiのスコアの最大値
for i in range(2):
    for j in range(N + 1):
        for k in range(K):
            if A[k] > j:
                break
            nj = j - A[k]
            dp[i][nj] = max(dp[i][nj], dp[i][j] + A[k])

print(max(dp[0]))
