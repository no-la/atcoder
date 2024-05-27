N, M, K = map(int, input().split())
MOD = 998244353

dp = [[0]*(K+1) for _ in range(N+1)]
# dp[i][j]: 長さiで和がjになるものの個数
dp[0][0] = 1

for i in range(1, N+1):
    for j in range(1,K+1):
        for k in range(1, M+1):
            if not (0<=j-k<K+1):
                continue
            dp[i][j] = (dp[i][j] + dp[i-1][j-k])%MOD

# print(*dp, sep="\n")
print(sum(dp[N])%MOD)

