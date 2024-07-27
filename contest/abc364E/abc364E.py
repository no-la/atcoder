N, X, Y = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
INF = 10**10

# dp[i][j][x]: A[:i]からj個食べて甘さx以下にするときの最小のしょっぱさ
dp = [[[INF]*(X+1) for _ in range(N+1)] for _ in range(N+1)]
dp[0][0] = [0]*(X+1)

ans = 0
for i in range(N):
    for j in range(i+1):
        for x in range(X):
            if dp[i][j][x]>Y:
                continue
            # A[i]を食べるとき
            nx = x+A[i][0]
            ans = max(ans, j+1)
            if nx<=X:
                dp[i+1][j+1][nx] = min(dp[i+1][j+1][nx], dp[i][j][x]+A[i][1])
                ans = max(ans, j+1)
            
            # A[i]を食べないとき
            dp[i+1][j][x] = min(dp[i+1][j][x], dp[i][j][x])

for i in range(N+1):
    for j in range(N+1):
        for x in range(X+1):
            if dp[i][j][x]<=Y and j<N:
                ans = max(ans, j+1)

print(ans)
# print(*dp, sep="\n")


