N, M = map(int, input().split())
d = [list(map(int, input().split())) for _ in range(N)]
INF = 10**13

e = [[INF] * (M + 1) for _ in range(N)]
# e[i][j]: ルーレットiでjポイント得るために払う金額の期待値
for i in range(N):
    e[i][0] = 0
    for j in range(M):
        for k in range(d[i][1]):
            nj = min(M, j + d[i][2 + k])
            e[i][nj] = min(e[i][nj], e[i][j] + d[i][0] / d[i][1])

# print(*e, sep="\n")

dp = [min([l[i] for l in e]) for i in range(M + 1)]
# dp[i]: iポイント得るために払う金額の期待値
print(*dp, sep="\n")
