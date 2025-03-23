"""WA"""

import sys
import bisect

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
d = [tuple(map(int, input().split())) for _ in range(N)]

# ソートして W について単調増加にする
# その後 H について LIS を求める
d.sort(key=lambda x: (x[0], x[1]))
INF = 10**10

dp = [INF] * (N + 1)
# dp[i]: 長さ i の増加部分列における最終要素の最小値
for i in range(N):
    j = bisect.bisect_left(dp, d[i][1])
    dp[j] = min(dp[j], d[i][1])

print(bisect.bisect_left(dp, INF))
