H, W = map(int, input().split())
S = [input() for _ in range(H)]
MOD = 10**9+7

dp = [[0]*(W+1) for _ in range(H+1)]
dp[1][1] = 1
dp[1][2] = -1
dp[2][1] = -1
dp[2][2] = -1

for k in range(3):
    for i in range(1, H+1):
        for j in range(1, W+1):
            if i==1 and j==1:
                continue
            if S[i-1][j-1]=="#":
                dp[i][j] = 0
                continue
            
            add = 0
            for l, (di, dj) in enumerate([(1, 0), (1, 1), (0, 1)]):
                if l==k:
                    continue
                add += dp[i-di][j-dj]
            dp[i][j] = (dp[i][j]+(add*2)%MOD)%MOD
            
            
            # あとは、移動の方向が変わる先に-dp[i][j]しておけばよい
            for l, (di, dj) in enumerate([(1, 0), (1, 1), (0, 1)]):
                if l==k:
                    continue
                ni, nj = i+di, j+dj
                if ni<=H and nj<=W and S[ni-1][nj-1]:
                    dp[ni][nj] = (dp[ni][nj]-dp[i][j])%MOD

            print("-"*20)
            print(i, j)
            print(*dp, sep="\n")
print(dp[H][W])
