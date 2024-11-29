N, M, K = map(int, input().split())
MOD = 998244353

dp = [[0] * (N + 1) for _ in range(K + 1)]
# dp[i][j]: i回でjにいる確率
dp[0][0] = 1

for i in range(K):
    for j in range(N):  # Nからは動かないようにする
        for x in range(1, M + 1):
            ni = i + 1
            nj = j + x
            if nj > N:
                nj = N - (nj % N)

            dp[ni][nj] += dp[i][j] * pow(M, -1, MOD)
            dp[ni][nj] %= MOD

ans = 0
for i in range(1, K + 1):
    ans += dp[i][N]
    ans %= MOD

print(ans)
