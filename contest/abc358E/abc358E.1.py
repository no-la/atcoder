MOD = 998244353

K = int(input())
C = list(map(int, input().split()))
N = 26

# 長さK以下
# 各文字iはC[i]個以下

dp = [[0]*(K+1) for _ in range(N+1)]
for i in range(N+1):
    dp[i][0] = 1
# dp[i][j]: 1, ..., iの文字を使って長さjの文字列を作る場合の数
for i in range(1, N+1):
    for j in range(1, K+1):
        comb = 1
        for k in range(C[i-1]+1):
            if j-k>=0:
                dp[i][j] = (dp[i][j]+(dp[i-1][j-k]*comb)%MOD)%MOD
            else:
                break
            comb = (comb*(j-k)*pow(k+1, -1, MOD))%MOD

# for d in dp:
#     print(*d)

print(sum(dp[N][1:])%MOD)
