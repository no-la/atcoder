N, X, Y = map(int, input().split())

dp_red = [[0, 0] for _ in range(N)]
dp_blue = [[0, 0] for _ in range(N)]
# dp_x[i]: レベルi+1のx色の宝石から赤、青が何個になるか
dp_red[0] = [1, 0]
dp_blue[0] = [0, 1]

for i in range(1, N):
    # 2つ目
    dp_blue[i][0] = 1*dp_red[i-1][0] + Y*dp_blue[i-1][0]
    dp_blue[i][1] = 1*dp_red[i-1][1] + Y*dp_blue[i-1][1]
    # 1つ目
    dp_red[i][0] = 1*dp_red[i-1][0] + X*dp_blue[i][0]
    dp_red[i][1] = 1*dp_red[i-1][1] + X*dp_blue[i][1]
    
print(dp_red[N-1][1])
# print(*dp_red, sep="\n")
# print("-"*20, *dp_blue, sep="\n")
