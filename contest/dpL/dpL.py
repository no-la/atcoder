import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
A = list(map(int, input().split()))

dp = [[-1] * (N + 1) for _ in range(N + 1)]
# dp[i][j]: A[i:j] が残っているときの X-Y の値
dp[0][N] = 0
for i in range(N):
    for j in range(N, i - 1, -1):
        if dp[i][j] == -1:
            continue
        t = (N - (j - i)) & 1

        if t == 0:
            # 太郎の番
            if i + 1 <= j:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + A[i])
                dp[i][j - 1] = max(dp[i][j - 1], dp[i][j] + A[j - 1])
        else:
            # 次郎の番
            if i + 1 <= j:
                dp[i + 1][j] = (
                    min(dp[i + 1][j], dp[i][j] - A[i])
                    if dp[i + 1][j] != -1
                    else dp[i][j] - A[i]
                )
                dp[i][j - 1] = (
                    min(dp[i][j - 1], dp[i][j] - A[j - 1])
                    if dp[i][j - 1] != -1
                    else dp[i][j] - A[j - 1]
                )

print(*dp, sep="\n")

for i in range(N):
    ...
