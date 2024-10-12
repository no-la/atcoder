"""TLE"""

N = int(input())
C = list(map(int, input().split()))

dp = [0] * (N + 1)
# dp[j]: j円以内での最大値

for j in range(N):
    for i in range(1, 10):
        nj = j + C[i - 1]
        if nj > N:
            continue
        dp[nj] = max(dp[nj], 10 * dp[j] + i)

print(dp[N])
