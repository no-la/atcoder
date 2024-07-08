N = int(input())
X, Y = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
INF = 10**10

dp = [[[INF]*(Y+1) for _ in range(X+1)] for _ in range(N)]
for i in range(N):
    dp[i][0][0] = 0
x, y = min(X, A[0][0]), min(Y, A[0][1])
dp[0][x][y] = 1
# dp[i][x][y]: 弁当0,...,iから選んでたこ焼きをx個、たい焼きをy個手に入れるための弁当の個数の最小値

for i in range(N-1):
    dx, dy = A[i+1]
    for x in range(X+1):
        for y in range(Y+1):
            nx, ny = min(X, x+dx), min(Y, y+dy)
            dp[i+1][nx][ny] = min(dp[i+1][nx][ny], dp[i][x][y] + 1)
            dp[i+1][x][y] = min(dp[i+1][x][y], dp[i][x][y])

# print(*dp, sep="\n")
print(dp[N-1][X][Y] if dp[N-1][X][Y]!=INF else -1)
