N = int(input())
S = input()

d = {"R":0, "P":1, "S":2}
dp = [[0]*3 for _ in range(N+1)]
# dp[i][s]: i回目にsを出した場合の勝利回数の最大値

for i in range(1, N+1):
    for s in d:
        if (d[S[i-1]]+1)%3 == d[s]: # S[i-1]に勝つとき
            dp[i][d[s]] = max(dp[i][d[s]], dp[i-1][(d[s]+1)%3]+1, dp[i-1][(d[s]+2)%3]+1)
        elif d[S[i-1]] == d[s]: # 引き分け
            dp[i][d[s]] = max(dp[i][d[s]], dp[i-1][(d[s]+1)%3], dp[i-1][(d[s]+2)%3])
        else:
            dp[i][d[s]] = 0

# print(*dp, sep="\n")
print(max(dp[N]))

