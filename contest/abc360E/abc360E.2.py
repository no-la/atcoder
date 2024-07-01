N, K = map(int, input().split())
MOD = 998244353

P = 2*pow(N, -2, MOD)%MOD # 黒が1以外から1へ動く確率
Q = (N**2-2*N+2)*pow(N, -2, MOD)%MOD # 黒がその位置から動かない確率

# 開始位置が1なので、1以外に行く確率はすべて等しい
dp = [0]*(K+1) # dp[i]: i回操作後に1にいる確率
dp[0] = 1
for i in range(1, K+1):
    dp[i] = Q*dp[i-1] + P*(1-dp[i-1])
    dp[i] %= MOD

ans = dp[K] + (1-dp[K])*(N+2)*pow(2, -1, MOD)
ans %= MOD
print(ans)
    