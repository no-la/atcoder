import sys

input = lambda: sys.stdin.readline().rstrip()
N, L = map(int, input().split())

dp = [0] * (N + 1)
dp[0] = 1
for i in range(N):
    dp[i + 1] += dp[i]
    dp[i + 1] %= 10**9 + 7
    if i + L <= N:
        dp[i + L] += dp[i]
        dp[i + L] %= 10**9 + 7

print(dp[N] % (10**9 + 7))
