S = input()
T = input()

dp = [[0] * (len(T) + 1) for _ in range(len(S) + 1)]
# dp[i][j]: S[:i]とT[:j]の最長の共通部分列の長さ

for i in range(1, len(S) + 1):
    for j in range(1, len(T) + 1):
        s, t = S[i - 1], T[j - 1]
        if s == t:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

ans = []
i, j = len(S), len(T)
while i > 0 and j > 0:
    if dp[i][j] == dp[i - 1][j - 1] + 1 and S[i - 1] == T[j - 1]:
        ans.append(S[i - 1])
        i -= 1
        j -= 1
    elif dp[i][j] == dp[i - 1][j]:
        i -= 1
    else:  # dp[i][j]==dp[i][j-1]
        j -= 1

print("".join(ans[::-1]))
# print(max(dp[len(S)]))
# print(*dp, "-" * 20, sep="\n")
# print(*_from, "-" * 20, sep="\n")
