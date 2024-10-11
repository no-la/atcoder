N, M = map(int, input().split())
A = list(map(int, input().split()))
MINF = -(10**15)

dp = [[MINF] * (M + 1) for _ in range(N)]
# dp[i][j]: A[i]まで見て部分列の長さがjであるときの最大値

dp[0][1] = A[0]
dp[0][0] = 0
for i in range(N - 1):
    for j in range(M):
        if dp[i][j] == MINF:
            continue
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + (j + 1) * A[i + 1])
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])

print(max([l[M] for l in dp]))
# print(*dp, sep="\n")
