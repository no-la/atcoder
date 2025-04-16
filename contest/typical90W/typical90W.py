"""NS"""

import sys

input = lambda: sys.stdin.readline().rstrip()
H, W = map(int, input().split())
C = [input() for _ in range(H)]
N = H * W
MOD = 10**9 + 7

# 二次元累積和というかdpというか
dp = [[[[0] * 2 for _ in range(N)] for _ in range(W + 1)] for _ in range(H + 1)]
# dp[i][j][k][x]: C[i][j]よりも右上に k 個置いて、C[i][j]に(x=0 なら置いてない、x=1 なら置く) 場合の数
for i in range(H + 1):
    dp[i][0][0][0] = 1
for j in range(W + 1):
    dp[0][j][0][0] = 1

for i in range(1, H + 1):
    for j in range(1, W + 1):
        for k in range(N):
            if k == 0:
                dp[i][j][k] = [1, 0]
                continue

            # dp[i-1][j][k][0] と dp[i][j-1][k][0] には重複があるので注意
            dp[i][j][k][0] = (
                dp[i - 1][j][k][1]
                + dp[i][j - 1][k][1]
                + dp[i - 1][j][k][0]
                + dp[i][j - 1][k][0]
                - sum(dp[i - 1][j - 1][k])
            )
            dp[i][j][k][0] %= MOD

            if C[i - 1][j - 1] == "#":
                dp[i][j][k][1] = 0
            else:
                dp[i][j][k][1] = (
                    dp[i - 1][j][k - 1][0]
                    + dp[i][j - 1][k - 1][0]
                    - sum(dp[i - 1][j - 1][k - 1])
                )
            dp[i][j][k][1] %= MOD


ans = 0
for k in range(N):
    ans += sum(dp[H][W][k])
    ans %= MOD

print(ans)
# print(*[[x[0] for x in dp[i]] for i in range(H + 1)], sep="\n")
# print(*[[x[1] for x in dp[i][1:]] for i in range(1, H + 1)], sep="\n")
