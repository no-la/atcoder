N, C = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
M = 30

def f(t, x, a):
    if t==1:
        return x&a
    elif t==2:
        return x|a
    else:
        return x^a

dp = [[[None]*(2) for _ in range(N+1)] for _ in range(M)]
# dp[k][i][x]: k桁目を見てx(= 0 or 1)に操作1, 1, 2, ..., 1, iを施した結果

for k in range(M):
    for x in range(2):
        dp[k][0][x] = x

for k in range(M):
    for i in range(N):
        t, a = A[i]
        a = (a&(1<<k))!=0
        for x in range(2):
            dp[k][i+1][x] = f(t, dp[k][i][dp[k][i][x]], a)

# print(*dp, sep="\n")

# 復元
for i in range(N):
    ans = 0
    for k in range(M):
        x = (C&(1<<k)) != 0
        ans += dp[k][i+1][x]*(1<<k)
        
    print(ans)
