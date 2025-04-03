import sys

input = lambda: sys.stdin.readline().rstrip()
N, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = 10**9 + 7

dp = [[0] * (K + 1) for _ in range(N + 1)]
# dp[i][j]: A[:i]に計j個配る場合の数
dp[0][0] = 1

for i in range(N):
    ni = i + 1
    for j in range(K + 1):
        l, r = j, j + A[i] + 1
        dp[ni][l] += dp[i][j]
        dp[ni][l] %= MOD
        if r < K + 1:
            dp[ni][r] -= dp[i][j]
            dp[ni][r] %= MOD
    for j in range(K):
        dp[ni][j + 1] += dp[ni][j]
        dp[ni][j + 1] %= MOD

print(dp[N][K])
