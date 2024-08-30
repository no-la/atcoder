N, M = map(int, input().split())
X = list(map(int, input().split()))
B = [0]*(N+1)
for _ in range(M):
    c, y = map(int, input().split())
    B[c] = y

dp = [[None]*(N+1) for _ in range(N+1)]
# dp[i][j]: i回コイントスをしてカウントがjのときの最大値

dp[0][0] = 0

for i in range(N):
    for j in range(N):
        if dp[i][j] is None:
            continue
        
        # 表
        v1 = dp[i][j] + X[i] + B[j+1]
        if dp[i+1][j+1] is None:
            dp[i+1][j+1] = v1
        else:
            dp[i+1][j+1] = max(dp[i+1][j+1], v1)
        
        # 裏
        v2 = dp[i][j] + B[0]
        if dp[i+1][0] is None:
            dp[i+1][0] = v2
        else:
            dp[i+1][0] = max(dp[i+1][0], v2)

print(max(dp[N]))
