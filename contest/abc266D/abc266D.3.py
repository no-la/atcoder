N = int(input())
d = [list(map(int, input().split())) for _ in range(N)]
M = 10**5

dp = [[None] * 5 for _ in range(M + 1)]
# dp[t][i]: 時刻tにiにいるときの最大値
dp[0][0] = 0

k = 0
for t in range(M):
    for i in range(5):
        if dp[t][i] is None:
            continue
        for j in range(i - 1, i + 2):
            if not (0 <= j < 5):
                continue
            # print(t, i, j)
            if dp[t + 1][j] is None:
                dp[t + 1][j] = dp[t][i]
            else:
                dp[t + 1][j] = max(dp[t + 1][j], dp[t][i])
    if k < N and t + 1 == d[k][0]:
        _, x, a = d[k]
        if dp[t + 1][x] is not None:
            dp[t + 1][x] += a
        k += 1

print(max([v for v in dp[M] if v is not None]))
# print(*dp, sep="\n")
