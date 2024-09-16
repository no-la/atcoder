N = int(input())

dp = [[0] * 3 for _ in range(N + 1)]
# dp[i][j]: i日目まで見て最後は活動jをしたときの幸福度の最大値

for i in range(N):
    A = list(map(int, input().split()))
    for j in range(3):
        dp[i + 1][j] = max(
            dp[i + 1][j], dp[i][(j + 1) % 3] + A[j], dp[i][(j + 2) % 3] + A[j]
        )

print(max(dp[N]))
