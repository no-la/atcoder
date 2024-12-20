N, K, D = map(int, input().split())
A = list(map(int, input().split()))

dp = [[[-1] * D for _ in range(K + 1)] for _ in range(N + 1)]
# dp[i][j][k]: A[:i]からj個選んだ和であり、和%D=kであるようなものの最大値
dp[0][0][0] = 0

for i in range(N):
    for j in range(K + 1):
        for k in range(D):
            if dp[i][j][k] == -1:
                continue
            # 選ぶ場合
            if j < K:
                dp[i + 1][j + 1][(k + A[i]) % D] = max(
                    dp[i + 1][j + 1][(k + A[i]) % D], dp[i][j][k] + A[i]
                )
            # 選ばない場合
            dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j][k])

print(dp[N][K][0])
