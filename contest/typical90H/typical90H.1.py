N = int(input())
S = input()
MOD = 10**9 + 7
M = 26
T = "atcoder"

dp = [[0] * (len(T) + 1) for _ in range(N + 1)]
# dp[i][j]: S[:i]からT[:j]を作る方法の数
for i in range(N + 1):
    dp[i][0] = 1

# 貰うDP
for i in range(1, N + 1):
    for j in range(1, len(T) + 1):
        if S[i - 1] == T[j - 1]:
            dp[i][j] += dp[i - 1][j - 1]
            dp[i][j] %= MOD

        dp[i][j] += dp[i - 1][j]
        dp[i][j] %= MOD


print(dp[N][len(T)])
