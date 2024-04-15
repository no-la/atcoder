N = int(input())
MOD = 998244353

ans = 0
dp = [[0]*11 for _ in range(N)]
# dp[i][j]: i+1桁目がjになる解きの場合の数

# 初期化
for j in range(1, 10):
    dp[0][j] = 1

for i in range(1, N):
    for j in range(1, 10):
        dp[i][j] = ((dp[i-1][j-1]%MOD + dp[i-1][j]%MOD)%MOD + dp[i-1][j+1]%MOD)%MOD
        # dp[i][j] = sum([dp[i-1][j-d] for d in range(-1, 2)])%MOD

for i in range(1, 10):
    ans = (ans+dp[N-1][i])%MOD
    
print(ans)
