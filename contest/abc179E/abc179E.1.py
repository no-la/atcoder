N, X, M = map(int, input().split())

# ダブリング
import math

MAX_OP = N  # 操作の最大回数
P_NUM = M  # 頂点の個数
DB_NUM = int(math.log2(MAX_OP)) + 1

# dp[i][j]: 頂点jから2^i回の操作後の頂点
dp = [[0] * P_NUM for _ in range(DB_NUM)]

# dp[0][0:X]を初期化
for i in range(P_NUM):
    dp[0][i] = i % M

# ダブリングで表を構築 O(P_NUM*logMAX_OP)
for k in range(1, DB_NUM):
    for n in range(P_NUM):
        dp[k][n] = dp[k - 1][dp[k - 1][n]]


# K回操作後の頂点を得る
K = N
now = X  # 始点
for i in range(DB_NUM):
    if K >> i & 1:
        now = dp[i][now]
