N, X = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

dp = [[False]*(N+1) for _ in range(10001)] # dp[i][j]: j回のジャンプで位置iに来れるかどうか
dp[0][0] = True
for j in range(1, N+1):
    for i in range(10001):
        for k in range(2):
            if 0<=i-A[j-1][k]<len(dp) and dp[i-A[j-1][k]][j-1]:
                dp[i][j] = True
print("Yes" if dp[X][N] else "No")