N = int(input())
S = input()
MOD = 10**9 + 7
M = 26
T = "atcoder"

dp = [[0] * (len(T) + 1) for _ in range(N + 1)]
# dp[i][j]: S[:i]からT[:j]を作る方法の数
for i in range(N + 1):
    dp[i][0] = 1

for i in range(N):
    for j in range(len(T)):
        if S[i] == T[j]:
            dp[i + 1][j + 1] += dp[i][j]
            dp[i + 1][j + 1] %= MOD

        if j != 0:
            dp[i + 1][j] += dp[i][j]
            dp[i + 1][j] %= MOD

    # (i, len(T)) -> (i+1, len(T)) の遷移が抜け落ちてるのでやる
    dp[i + 1][len(T)] += dp[i][len(T)]
    dp[i + 1][len(T)] %= MOD

print(dp[N][len(T)])
# print(*dp, sep="\n")
