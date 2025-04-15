"""小課題3"""

import sys

input = lambda: sys.stdin.readline().rstrip()
N, B, K = map(int, input().split())
C = list(map(int, input().split()))
MOD = 10**9 + 7

# ダブリング
import math

MAX_OP = N  # 操作の最大回数
P_NUM = B  # 頂点の個数
DB_NUM = int(math.log2(MAX_OP)) + 1

# 準備
pow10 = [0] * (DB_NUM + 1)
# pow10[i]: 10^(2^i) mod B
pow10[0] = 10
for i in range(1, DB_NUM + 1):
    pow10[i] = pow(pow10[i - 1], 2, B)

# dp[i][j]: 2^i桁 で mod B で j になる数の個数
dp = [[0] * P_NUM for _ in range(DB_NUM)]

# dp[0][0:X]を初期化
for c in C:
    dp[0][c % B] += 1

for k in range(1, DB_NUM):
    for i in range(B):
        for j in range(B):
            nex = (i * pow10[k - 1] + j) % B
            dp[k][nex] += dp[k - 1][i] * dp[k - 1][j]
            dp[k][nex] %= MOD


ans = [0] * B
ans[0] = 1
# ans[i]: 今見ている桁数で mod B で i になる数の個数
for k in range(DB_NUM):
    if N >> k & 1:
        temp = [0] * B
        for i in range(B):
            for j in range(B):
                nex = (i * pow10[k] + j) % B
                temp[nex] += ans[i] * dp[k][j]
                temp[nex] %= MOD
        ans = temp

print(ans[0])
# print(ans)
