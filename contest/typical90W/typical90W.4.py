"""小課題3 NS"""

from collections import defaultdict
import sys

input = lambda: sys.stdin.readline().rstrip()
H, W = map(int, input().split())
C = [input() for _ in range(H)]
N = 200000
MOD = 10**9 + 7

if H > 9 or W > 9:
    print("MURI☆")
    exit()


def can_put(k, x):
    i, j = divmod(k - 1, W)
    if i == 0:
        return j == 0 or x & (1 << W) == 0
    if j == 0:
        return x & 2 == 0 and x & 4 == 0
    if j == W - 1:
        return not (x & 1 or x & 2 or x & (1 << W))

    return not (x & 1 or x & 2 or x & 4 or x & (1 << W))


dp = [defaultdict(int) for _ in range(H * W + 1)]
dp[0][0] = 1
# dp[k][x]: マス k を、直前のW+1マスの状態が x として見たときの場合の数
# x はbitで持つ

# 状態の遷移を先に作っておく
X = set([0])


def f(x: int):
    y = (x >> 1) + (1 << W)
    z = x >> 1
    if (y & W == 0 or y & (W + 1) == 0) and y not in X:
        X.add(y)
        f(y)
    if z not in X:
        X.add(z)
        f(z)


f(0)

for k in range(H * W):
    for x in X:
        i, j = divmod(k, W)
        y = (x >> 1) + (1 << W)
        z = x >> 1
        # マス k+1 に置くとき
        if C[i][j] == "." and can_put(k + 1, x):
            dp[k + 1][y] += dp[k][x]
            dp[k + 1][y] %= MOD

        # マス k+1 に置かないとき
        dp[k + 1][z] += dp[k][x]
        dp[k + 1][z] %= MOD

print(sum(dp[H * W]) % MOD)
if len(X) < 50:
    print(X)
