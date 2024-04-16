N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
M = max([a[0] for a in A])+1

dp = [[0]*5 for _ in range(M)]
# dp[i][j]: 時刻iに座標jにいるときの最大値

c = 0
for i in range(1, M):
    for j in range(min(i+1, 5)):
        dp[i][j] = dp[i-1][j]
        dp[i][j] = max([
            dp[i-abs(j-k)][k] for k in range(min(i+1, 5)) if 0<=i-abs(j-k)])
        if A[c][0]==i and A[c][1]==j:
            # print(i, j, "add", A[c][2])
            dp[i][j] += A[c][2]
    if A[c][0]==i:
        c += 1


# print(*dp, sep="\n")
print(max(dp[-1]))