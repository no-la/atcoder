N = int(input())
H = list(map(int, input().split()))
M = max(H)

dp = [[1] * N for _ in range(N)]
# dp[i][j]: 最後がH[i]で幅がjのときの最長の要素数

for i in range(N - 1):
    for j in range(1, N):
        ni = i + j
        if ni < N and H[i] == H[ni]:
            dp[ni][j] = max(dp[ni][j], dp[i][j] + 1)

print(max([max(dp[i]) for i in range(N)]))
