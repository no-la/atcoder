import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
A = list(map(int, input().split()))
INF = 10**18

dp = [[-INF] * (N + 1) for _ in range(N + 1)]
# dp[i][j]: A[i:j] が残っている状態で始めたときの最終的な X-Y の値
for i in range(N):
    dp[i][i + 1] = A[i]

for k in range(1, N + 1):
    # k は残っている要素数
    for i in range(N - k + 1):
        j = i + k
        # A[i:j] が残っているとき
        ni, nj = i - 1, j + 1
        if ni >= 0:
            dp[ni][j] = max(dp[ni][j], -dp[i][j] + A[ni])
        if nj <= N:
            dp[i][nj] = max(dp[i][nj], -dp[i][j] + A[nj - 1])

print(dp[0][N])
