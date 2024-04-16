N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
M = max([a[0] for a in A])

dp = [[0]*6 for _ in range(M)]
# dp[i][j]: 時刻iに座標jにいるときの最大値

c = 0
for i in range(M):
    for j in range(1, 6):
        for k in range(-5, 6):
            if c>=N:
                break
            if not (0<=i-k<M and 1<=j+k<6):
                continue
            
            v = dp[i-k][k]
            if A[c][0]==i and A[c][1]==k:
                v += A[c][2]
            
            if A[c][0]<=i:
                c += 1
            dp[i][j] = max(dp[i][j], v)


print(*dp, sep="\n")
print(max(dp[-1]))