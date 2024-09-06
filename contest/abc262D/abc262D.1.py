N = int(input())
A = list(map(int, input().split()))
MOD = 998244353


ans = 0
for k in range(1, N+1): # k項選ぶとき
    dp = [[[0]*k for _ in range(k+1)] for _ in range(N+1)]
    # dp[i][j][x]: A[:i]からj項選んで平均値がx(mod k)である場合の数
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(k+1):
            for x in range(k):
                # print(k, i, j, x)
                # A[i]を選ぶとき
                if j+1<=k:
                    # print(1, f"{dp[i+1][j+1][(x+A[i])%k]=}, {dp[i][j][x]=}")
                    dp[i+1][j+1][(x+A[i])%k] += dp[i][j][x]
                    dp[i+1][j+1][(x+A[i])%k] %= MOD
                # A[i]を選ばないとき
                # print(0, f"{dp[i+1][j][x]=}, {dp[i][j][x]=}")
                dp[i+1][j][x] += dp[i][j][x]
                dp[i+1][j][x] %= MOD
    # print(k, *dp, "-"*20, sep="\n")
    ans += dp[N][k][0]
    ans %= MOD

print(ans)
