N = int(input())
A = list(map(int, input().split()))
MOD = 998244353
from collections import defaultdict
dp = [[defaultdict(int) for _ in range(N+1)] for _ in range(N)]
# dp[i][k][d]: 末項A[i]、長さk、交差dの部分列

for i in range(N):
    dp[i][1] = defaultdict(lambda:1)


for i in range(N):
    for k in range(1, N+1):
        for j in range(i):
            d = A[i]-A[j]
            dp[i][k][d] += dp[j][k-1][d]
            dp[i][k][d] %= MOD

ans = [0]*(N+1)
ans[1] = N
for i in range(N):
    for k in range(2, N+1):
        ans[k] += sum(dp[i][k].values())%MOD
        ans[k] %= MOD


# for l in dp:
#     print(list(map(lambda a:dict(a), l)))
print(*ans[1:])
