H, W = map(int, input().split())
S = [input() for _ in range(H)]
MOD = 10**9+7

dp = [[0]*(W+1) for _ in range(H+1)] # dp[i][j]: マスi, jに行く場合の数

for i in range(1, H+1):
    for j in range(1, W+1):
        if i==1 and j==1:
            dp[1][1] = 1
        else:
            dp[i][j] = (S[i-1][j-1]==".")*(dp[i-1][j]+dp[i-1][j-1]+dp[i][j-1])%MOD


print(*dp, sep="\n")
print(dp[H][W])
