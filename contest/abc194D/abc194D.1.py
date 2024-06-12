N = int(input())

dp = [0]*(N+1)
# dp[i]: i個の頂点が連結になるための操作回数の期待値
# i個の頂点が連結のとき、i+1個の頂点が連結になるための操作回数の期待値は
# (N-i)/N + i(N-i)/N^2 * 2 + ... + i^(k-1)(N-i)/N^k * k + ...
dp[1] = 0

for i in range(1, N):
    dp[i+1] = dp[i] + N/(N-i)

# print(*dp)
print(f"{dp[-1]:.11f}")
