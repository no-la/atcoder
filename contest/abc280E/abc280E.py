N, P = map(int, input().split())
MOD = 998244353

P = P * pow(100, -1, MOD) % MOD
Q = (1 - P) % MOD

dp = [0] * (N + 1)
# dp[i]: 体力iを0以下にするための攻撃回数の期待値
dp[1] = 1

for i in range(2, N + 1):
    dp[i] = (dp[i - 1] + 1) * Q + (dp[i - 2] + 1) * P
    dp[i] %= MOD

print(dp[N])
