"""AC"""

S = input()
T = input()

dp = [[0] * (len(T) + 1) for _ in range(len(S) + 1)]
# dp[i][j]: S[:i]とT[:j]の最長の共通部分列の長さ

_from = [[None] * (len(T) + 1) for _ in range(len(S) + 1)]

for i, s in enumerate(S):
    for j, t in enumerate(T):
        if dp[i + 1][j + 1] < dp[i][j] + (s == t):
            if s == t:
                dp[i + 1][j + 1] = dp[i][j] + 1
                _from[i + 1][j + 1] = (i, j)
            else:
                dp[i + 1][j + 1] = dp[i][j]
                _from[i + 1][j + 1] = _from[i][j]

        if dp[i][j + 1] < dp[i][j]:
            dp[i][j + 1] = dp[i][j]
            _from[i][j + 1] = _from[i][j]

        if dp[i + 1][j] < dp[i][j]:
            dp[i + 1][j] = dp[i][j]
            _from[i + 1][j] = _from[i][j]

# 端の処理
for j in range(len(T)):
    if dp[len(S)][j + 1] < dp[len(S)][j]:
        dp[len(S)][j + 1] = max(dp[len(S)][j + 1], dp[len(S)][j])
        _from[len(S)][j + 1] = _from[len(S)][j]
for i in range(len(S)):
    if dp[i + 1][len(T)] < dp[i][len(T)]:
        dp[i + 1][len(T)] = max(dp[i][len(T)], dp[i][len(T)])
        _from[i + 1][len(T)] = _from[i][len(T)]

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
