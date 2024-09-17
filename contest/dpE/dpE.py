"""TLE解"""

from collections import defaultdict

N, W = map(int, input().split())

dp = [defaultdict(int) for _ in range(N + 1)]
dp[0][0] = 0

for i in range(N):
    w, v = map(int, input().split())
    for j in dp[i].keys():
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
        if j + w <= W:
            dp[i + 1][j + w] = max(dp[i + 1][j + w], dp[i][j] + v)

print(max(dp[N].values()))
