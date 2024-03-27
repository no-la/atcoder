R, C, K = map(int, input().split())
D = [[0]*C for _ in range(R)]
for _ in range(K):
    r, c, v = map(int, input().split())
    r -= 1
    c -= 1
    D[r][c] = v
# dp[i][j][k]: (i,j)に行くまでに拾うアイテムの価値の最大値で、特にi行目はk個以下拾うとする
dp = [[[0, 0, 0, 0] for _ in range(C+1)] for _ in range(R+1)]
for i in range(1, R+1): # O(4CR) < 4*3000^2 = 1.2*10^7
    for j in range(1, C+1):
        for k in range(4):
            temp = []
            temp.append(dp[i-1][j][3]) # upのときは行が変わるので、kはなんでもいい
            temp.append(dp[i][j-1][k])
            if k!=0:
                temp.append(dp[i-1][j][3] + D[i-1][j-1])
                temp.append(dp[i][j-1][k-1] + D[i-1][j-1])
            dp[i][j][k] = max(temp)

print(max(dp[-1][-1]))
# print(*D, sep="\n")
# for k in range(4):
#     print("k =", k)
#     print(*[[b[k] for b in a] for a in dp], sep="\n")