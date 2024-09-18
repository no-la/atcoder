S = input()
T = input()

dp = [[0] * (len(T) + 1) for _ in range(len(S) + 1)]
# dp[i][j]: S[:i]とT[:j]の最長の共通部分列

for i, s in enumerate(S):
    for j, t in enumerate(T):
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + (s == t))
        dp[i][j + 1] = max(dp[i][j + 1], dp[i][j])
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])

print(max(dp[len(S)]))
print(*dp, sep="\n")
