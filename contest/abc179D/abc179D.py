N, K = map(int, input().split())
LR = [tuple(map(int, input().split())) for _ in range(N)]
MOD = 998244353

# 移動

dp = [0]*(N+1) # dp[i]: マスiに行く方法の個数
dp[0] = 1

for i in range(1, N):
    for l, r in LR:
        ...