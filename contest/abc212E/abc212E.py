N, M, K = map(int, input().split())
MOD = 998244353
D = [[] for _ in range(N)] # D[i]: iから進めない頂点
for _ in range(M):
    u, v = map(lambda x: int(x)-1, input().split())
    D[u].append(v)
    D[v].append(u)

for i in range(N):
    D[i].sort()

# print(*D, sep="\n")
# print("-"*20)

# dpとimos?
dp = [[0]*N for _ in range(K+2)]
dp[1][0] = 1
# dp[k][i]: 長さkのパス0->...->iの個数

for k in range(1, K+1):
    # imos法
    for i in range(N):
        # iから進める頂点jに、dp[k+1][j] += dp[k][i]
        dp[k+1][0] += dp[k][i]
        dp[k+1][0] %= MOD
        dp[k+1][i] -= dp[k][i]
        dp[k+1][i] %= MOD
        if i+1<N:
            dp[k+1][i+1] += dp[k][i]
            dp[k+1][i+1] %= MOD
        for j in D[i]: # このループは合計でO(M)
            dp[k+1][j] -= dp[k][i]
            dp[k+1][j] %= MOD
            if j+1<N:
                dp[k+1][j+1] += dp[k][i]
                dp[k+1][j+1] %= MOD
    
    # print(k+1, dp[k+1])
    for i in range(1, N):
        dp[k+1][i] += dp[k+1][i-1]
        dp[k+1][i] %= MOD


# print("-"*20, *dp, sep="\n")

print(dp[k+1][0])
