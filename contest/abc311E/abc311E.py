H, W, N = map(int, input().split())
D = [[1]*W for _ in range(H)]
for _ in range(N):
    a, b = map(lambda x: int(x)-1, input().split())
    D[a][b] = 0


dp = [[0]*(W+1) for _ in range(H+1)]
dp[H-1][W-1] = D[H-1][W-1]
# dp[i][j]: (i, j)を左上とする「穴のない正方形」の個数
# 右下からいい感じに更新できるんじゃないでしょうか

down = [[0]*W for _ in range(H)]
right = [[0]*W for _ in range(H)]
for i in range(H):
    nearest = W
    for j in range(W-1, -1, -1):
        if not D[i][j]:
            nearest = j
        right[i][j] = nearest
for j in range(W):
    nearest = H
    for i in range(H-1, -1, -1):
        if not D[i][j]:
            nearest = i
        down[i][j] = nearest

# print(*right, "-"*20, sep="\n")
# print(*down, "-"*20, sep="\n")

for i in range(H-1,-1, -1):
    for j in range(W-1, -1, -1):
        dp[i][j] = min(dp[i+1][j+1]+1, right[i][j]-j, down[i][j]-i)

# print(*dp, sep="\n")
ans = 0
for i in range(H):
    for j in range(W):
        ans += dp[i][j]

print(ans)
