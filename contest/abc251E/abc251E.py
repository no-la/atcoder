N = int(input())
A = list(map(int, input().split()))
INF = 10**15

# A[0]を選ぶときと選ばない時で場合分けする
# A[0]を選ぶとき
dp = [[INF] * 2 for _ in range(N + 1)]
# dp[i][j]: 0,...,i-1種類目までの行動をするかしないかを決めて、動物0,...,i+j-1に餌をあげたときの費用の最小値
dp[0][0] = 0
dp[1][0] = A[0]

for i in range(N):
    dp[i + 1][1] = min(dp[i + 1][1], dp[i][0] + A[i], dp[i][1] + A[i])
    dp[i + 1][0] = min(dp[i + 1][0], dp[i][1])

# print(dp)
ans = min(dp[N])

# A[0]を選ばないとき
# A[N-1]を選ぶ必要がある
dp = [[INF] * 2 for _ in range(N + 1)]
dp[0][0] = A[N - 1]
dp[1][0] = A[N - 1]

for i in range(N - 1):
    dp[i + 1][1] = min(dp[i + 1][1], dp[i][0] + A[i], dp[i][1] + A[i])
    dp[i + 1][0] = min(dp[i + 1][0], dp[i][1])

ans = min(ans, dp[N - 1][0])
# print(dp)
print(ans)
