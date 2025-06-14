import sys

input = lambda: sys.stdin.readline().rstrip()
N, H, M = map(int, input().split())
d = [list(map(int, input().split())) for _ in range(N)]
INF = float("inf")

dp = [[INF] * (H + 1) for _ in range(N + 1)]
dp[0][0] = 0
# dp[i][h]: i 番目まで見て減った体力が h のときの 減った魔力の最小値

for i in range(N):
    for h in range(H + 1):
        if dp[i][h] == INF:
            continue

        nh = h + d[i][0]
        if nh <= H:
            dp[i + 1][nh] = min(dp[i + 1][nh], dp[i][h])
        dp[i + 1][h] = min(dp[i + 1][h], dp[i][h] + d[i][1])

ans = 0
for i in range(N + 1):
    for h in range(H + 1):
        if dp[i][h] <= M:
            ans = max(ans, i)

print(ans)
# print(*dp, sep="\n")
