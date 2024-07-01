N, M, K = map(int, input().split())
MOD = 998244353

dp = [[0]*(M+1) for _ in range(N+1)]
# dp[i][j]: 長さiの数列で最後の数字がjのときの答え
dp[1] = [1]*(M+1)
dp[1][0] = 0
for i in range(1, N):
    b = [0]*(M+1) # dp[i+1]の階差数列
    for j in range(1, M+1):
        if 1<=j-K==j+K<=M:
            b[1] += dp[i][j]
            b[1] %= MOD
            continue
        if 1<=j-K:
            b[1] += dp[i][j]
            b[1] %= MOD
            if j-K+1<=M:
                b[j-K+1] -= dp[i][j]
                b[j-K+1] %= MOD
        if j+K<=M:
            b[max(1, j+K)] += dp[i][j]
            b[max(1, j+K)] %= MOD
    
    for j in range(1, M+1):
        dp[i+1][j] = dp[i+1][j-1] + b[j]
        dp[i+1][j] %= MOD

ans = 0
for j in range(1, M+1):
    ans += dp[N][j]
    ans %= MOD

# print(*dp, sep="\n")
print(ans)
