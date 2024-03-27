R, C, K = map(int, input().split())
D = [[0]*C for _ in range(R)]
for _ in range(K):
    r, c, v = map(int, input().split())
    r -= 1
    c -= 1
    D[r][c] = v
# dp[i][j]: (i,j)に行くまでに拾うアイテムの価値の最大値で、特にi行目はk+1個拾うとする
dp = [[[0]*3 for _ in range(C+1)] for _ in range(R+1)]
for i in range(1, R+1): # O(4CR) < 4*3000^2 = 1.2*10^7
    for j in range(1, C+1):
        dp[i][j][0] = max((*[a+D[i-1][j-1] for a in dp[i-1][j]], dp[i][j-1][0]))
        for k in range(1, 3):
            dp[i][j][k] = max(dp[i][j-1][k-1]+D[i-1][j-1], dp[i][j-1][k])

print(max([dp[-1][-1][k] for k in range(3)]))
# print(*D, sep="\n")
# for k in range(3):
#     print("k =", k)
#     print(*[[b[k] for b in a] for a in dp], sep="\n")