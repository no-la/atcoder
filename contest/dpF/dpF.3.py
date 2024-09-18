S = input()
T = input()

dp = [[0] * (len(T) + 1) for _ in range(len(S) + 1)]
# dp[i][j]: S[:i]とT[:j]の最長の共通部分列の長さ

_from = [[None] * (len(T) + 1) for _ in range(len(S) + 1)]

for i in range(1, len(S) + 1):
    for j in range(1, len(T) + 1):
        s, t = S[i - 1], T[j - 1]
        if s == t:
            dp[i][j] = dp[i - 1][j - 1] + 1
            _from[i][j] = (i - 1, j - 1)
        elif dp[i][j - 1] > dp[i - 1][j]:
            dp[i][j] = dp[i][j - 1]
            _from[i][j] = _from[i][j - 1]
        else:
            dp[i][j] = dp[i - 1][j]
            _from[i][j] = _from[i - 1][j]


ans = []
if _from[len(S)][len(T)] is not None:
    i, j = _from[len(S)][len(T)]
    while True:
        ans.append(S[i])
        if _from[i][j] is None:
            break
        i, j = _from[i][j]

print("".join(ans[::-1]))
# print(max(dp[len(S)]))
# print(*dp, "-" * 20, sep="\n")
# print(*_from, "-" * 20, sep="\n")
