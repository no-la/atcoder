N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
M = max([a[0] for a in A])+1

dp = [[0]*5 for _ in range(M)]
# dp[i][j]: 時刻iに座標jにいるときの最大値

c = 0
for i in range(1, M):
    for j in range(min(i, 5)):
        dp[i][j] = dp[i-1][j]
        for k in range(min(i, 5)): # k->j
            if c>=N:
                break
            t = i-abs(j-k)
            if 0>t:
                continue
            v = dp[t][k]
            # print(i, k, "->", j, "by", t)
            if A[c][0]==i:
                if A[c][1]==j:
                    v += A[c][2]
            dp[i][j] = max(dp[i][j], v)
            
    if A[c][0]==i:
        c += 1


print(*dp, sep="\n")
print(max(dp[-1]))