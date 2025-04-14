"""小課題1"""

import sys

input = lambda: sys.stdin.readline().rstrip()
N, B, K = map(int, input().split())
C = list(map(int, input().split()))
MOD = 10**9 + 7

if N > 10000:
    print("MURI☆")
    exit()

dp = [[0] * B for _ in range(N + 1)]
# dp[i][j]: 上からi桁目まで見て MOD B で j になる数の個数
dp[0][0] = 1
for i in range(N):
    for j in range(B):
        for c in C:
            dp[i + 1][(j * 10 + c) % B] += dp[i][j]
            dp[i + 1][(j * 10 + c) % B] %= MOD

print(dp[N][0])
