import math

N, X = map(int, input().split())
P = list(map(lambda x: int(x) / 100, input().split()))
INF = 10**15

q = [[0] * (N + 1) for _ in range(N + 1)]
# q[i][j]: 1回の操作でP[:i]からレアカードをj枚手に入れる確率
q[0][0] = 1
for i in range(N):
    for j in range(N):
        q[i + 1][j] += q[i][j] * (1 - P[i])
        q[i + 1][j + 1] += q[i][j] * P[i]

# print(*q, sep="\n")
Q = q[-1]
# Q[i]: 1回の操作でi枚のレアカードを手に入れる確率

dp = [INF] * (X + 1)
# dp[i]: i枚手に入れるときの操作回数の期待値
dp[0] = 0
for i in range(X):
    for j in range(1, N + 1):
        dp[i]
