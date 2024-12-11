N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = [1] * (K + 1)
# dp[i]: i個残っているときの勝者
dp[0] = 1

for i in range(1, K + 1):
    for a in A:
        if i - a >= 0 and dp[i - a] == 1:
            dp[i] = 0
            break

# print(dp)
print(["First", "Second"][dp[K]])
