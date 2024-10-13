"""AC"""

N = int(input())
d = [list(map(int, input().split())) for _ in range(N)]
B_SUM = sum([v[1] for v in d])
INF = N + 1

if B_SUM % 3 != 0:
    print(-1)
    exit()

M = B_SUM // 3
S = [0, 0, 0]
for i in range(N):
    d[i][0] -= 1  # to 0-indexed
    S[d[i][0]] += d[i][1]

cumsum = [[0] * (N + 1) for _ in range(3)]
for i in range(3):
    for j in range(N):
        cumsum[i][j + 1] = cumsum[i][j] + (i == d[j][0]) * d[j][1]

dp = [[[INF] * (M + 1) for _ in range(M + 1)] for _ in range(N + 1)]
# dp[i][j][k]: d[:i]までを確定して各チームの強さをj, k, cumsum[2][i]-j-kにするための移動回数の最小値
for i in range(N + 1):
    if cumsum[0][i] <= M and cumsum[1][i] <= M:
        dp[i][cumsum[0][i]][cumsum[1][i]] = 0

for i in range(N):
    team, strength = d[i]
    for j in range(M + 1):
        for k in range(M + 1):
            l = 0  # なんでもいい
            for a in range(3):
                nteam = (team + a) % 3
                temp = [j, k, l]
                temp[nteam] += strength
                nj, nk, nl = temp
                if nj > M or nk > M:
                    continue
                dp[i + 1][nj][nk] = min(
                    dp[i + 1][nj][nk], dp[i][j][k] + (team != nteam)
                )

print(dp[N][M][M] if dp[N][M][M] < INF else -1)
# print(*dp, sep="\n")
