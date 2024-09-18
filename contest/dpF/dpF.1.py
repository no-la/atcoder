S = input()
T = input()

dp = [[["", -1] for _ in range(2)] for _ in range(len(S) + 1)]
# dp[i][j]: [S[:i]とTの最長の共通部分列で、S[i-1]を選ぶ or 選ばないもの(j), 使ったTのindex]


for i, s in enumerate(S):
    dp[i + 1][1] = dp[i]
    for j in range(dp[i][1] + 1, len(T)):
        if s == T[j]:
            dp[i + 1][0] = [dp[i][0] + s, j]


print(max(dp[len(S)]))
print(*dp, sep="\n")
