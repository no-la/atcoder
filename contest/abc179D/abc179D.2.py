N, K = map(int, input().split())
LR = [tuple(map(int, input().split())) for _ in range(K)]
MOD = 998244353


dp = [0]*N # dp[i]: i+1まで行く方法の個数
b = [0]*N # b[i]: dp[i]-dp[i-1], 階差数列
dp[0] = 1 # 初期化
b[1] = -1 # 初期化
for i in range(N):
    if i>=1:
        dp[i] = (dp[i-1] + b[i])%MOD
    for l, r in LR:
        nl, nr = i+l, i+r+1
        if nl<N:
            b[nl] = (b[nl]+dp[i])%MOD
        if nr<N:
            b[nr] = (b[nr]-dp[i])%MOD
        
print(dp[N-1])