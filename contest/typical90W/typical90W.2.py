"""小課題2"""

import sys

input = lambda: sys.stdin.readline().rstrip()
H, W = map(int, input().split())
C = [input() for _ in range(H)]
N = 2**W
MOD = 10**9 + 7

if H > 9 or W > 9:
    print("MURI☆")
    exit()

dp = [[0] * N for _ in range(H + 1)]
dp[0][0] = 1
# dp[i][x]: i行目の盤面が x のときの場合の数
# x はbitで、立っている部分には置かれているものとする

# 昇順に見ていくとき、i行目の値はi-1行目のみに依存することに注意する


def check_white(x: int, c: list):
    for i in range(W):
        if x & (1 << i) and c[i] == "#":
            return False
    return True


def check_king(x: int, y: int):
    for i in range(W):
        if x & (1 << i) == 0:
            continue
        if x & (1 << (i + 1)):
            return False
        for j in range(max(0, i - 1), min(i + 2, W)):
            if y & (1 << j):
                return False
    return True


for i in range(1, H + 1):
    for x in range(N):
        if not check_white(x, C[i - 1]):
            continue
        for y in range(N):
            if check_king(x, y):
                dp[i][x] += dp[i - 1][y]
                dp[i][x] %= MOD

print(sum(dp[H]) % MOD)
