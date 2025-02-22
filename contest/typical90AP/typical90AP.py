import sys

input = lambda: sys.stdin.readline().rstrip()
K = int(input())
MOD = 10**9 + 7

if K % 9 != 0:
    print(0)
    exit()

dp = [0] * (K + 1)
# dp[i]: 各桁の和がiであるような場合の数
dp[0] = 1
for i in range(K):
    for j in range(1, 10):
        ni = i + j
        if ni > K:
            break
        dp[ni] += dp[i]
        dp[ni] %= MOD

# print(dp)
print(dp[K] % MOD)
