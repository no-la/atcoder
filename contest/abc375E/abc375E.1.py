"""TLE"""

from collections import defaultdict

N = int(input())
d = [list(map(int, input().split())) for _ in range(N)]
B_SUM = sum([v[1] for v in d])
INF = 100

if B_SUM % 3 != 0:
    print(-1)
    exit()

M = B_SUM // 3
S = [0, 0, 0]
for i in range(N):
    d[i][0] -= 1  # to 0-indexed
    S[d[i][0]] += d[i][1]

# dp = [[[INF] * (B_SUM + 1) for _ in range(B_SUM + 1)] for _ in range(N + 1)]
dp = [defaultdict(lambda: defaultdict(lambda: INF)) for _ in range(N + 1)]
# dp[i][j][k]: d[:i]ま動かして見て各チームの強さをj, k, B_SUM-i-jにするための移動回数の最小値
dp[0][S[0]][S[1]] = 0

for i in range(N):
    team, strength = d[i]
    for j in dp[i].keys():
        for k in dp[i][j].keys():
            if dp[i][j][k] == INF:
                continue
            l = B_SUM - j - k
            dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])
            for a in range(1, 3):
                nteam = (team + a) % 3
                temp = [j, k, l]
                temp[team] -= strength
                temp[nteam] += strength
                nj, nk, _ = temp
                dp[i + 1][nj][nk] = min(dp[i + 1][nj][nk], dp[i][j][k] + 1)

print(dp[N][M][M])
# print(*dp, sep="\n")
