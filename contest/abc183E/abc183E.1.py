# https://atcoder.jp/contests/abc183/submissions/52428731
H, W = map(int, input().split())
S = [input() for _ in range(H)]
MOD = 10**9+7

dp = [[0]*(W+1) for _ in range(H+1)] # dp[i][j]: マスi,jに行く方法の数

hor = [[0]*(W+1) for _ in range(H+1)] # hor[i][j]: dp[i][_]の累積和
ver = [[0]*(W+1) for _ in range(H+1)] # ver[i][j]: dp[_][j]の累積和
dia = [[0]*(W+1) for _ in range(H+1)] # hor[i][j]: dp[i+_][j+_]の累積和

for i in range(1, H+1):
    for j in range(1, W+1):        
        if i==1 and j==1:
            dp[i][j] = 1
        elif S[i-1][j-1]=="#":
            dp[i][j] = 0
            hor[i][j] = 0
            ver[i][j] = 0
            dia[i][j] = 0
        else:
            hor[i][j] = (hor[i][j-1] + dp[i][j-1])%MOD
            ver[i][j] = (ver[i-1][j] + dp[i-1][j])%MOD
            dia[i][j] = (dia[i-1][j-1] + dp[i-1][j-1])%MOD
        
            dp[i][j] = (hor[i][j]+ver[i][j]+dia[i][j])%MOD

# print("-"*20)
# print(*dp, sep="\n")
print(dp[-1][-1])