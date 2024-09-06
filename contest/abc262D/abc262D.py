N = int(input())
A = list(map(int, input().split()))
MOD = 998244353

dp = [[[0]*(k+1) for k in range(N+1)] for _ in range(N+1)]
# dp[i][k][x]: A[:i]からk項選んで平均値がx(mod k+1)である場合の数

for i in range(N):
    for k in range(N):
        for x in range(k+1):
            # A[i]を選ぶとき
            dp[i+1][k+1][(x+A[i])%(k+2)] += dp[i][k][x]
            dp[i+1][k+1][(x+A[i])%(k+2)] %= MOD
            # A[i]を選ばないとき
            dp[i+1][k][]
