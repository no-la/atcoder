N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
INF = 10**13
S = sum([A[i][2] for i in range(N)])

dp = [[INF]*(S+1) for _ in range(N+1)]
# dp[i][j]: A[:i]を変えてj議席獲得するために必要な鞍替えする人数の最小値

v = sum([(a[0]>a[1])*a[2] for a in A])
for i in range(N+1):
    for j in range(S+1):
        if j<=v:
            dp[i][j] = 0

# print(S, v)
# print(*dp, sep="\n")
for i in range(N):
    for j in range(S):
        # A[i]の議席を新たに獲得するとき
        if A[i][0]<A[i][1]:
            nj = min(S, j+A[i][2])
            dp[i+1][nj] = min(dp[i+1][nj], dp[i][j] + (A[i][1]-A[i][0]+1)//2)
        
        # しないとき
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])

# print(*dp, sep="\n")
print(min(dp[N][(S+1)//2:]))

