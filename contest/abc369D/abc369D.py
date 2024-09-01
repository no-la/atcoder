N = int(input())
A = list(map(int, input().split()))


dp = [[0]*2 for _ in range(N+1)]
# dp[i][x]: i匹目まで終って、最後に倒したのが偶数(x=0)または奇数(x=1)匹目であるときの最大値
dp[0][0] = 0
dp[0][1] = None

for i in range(N):
    for x in range(2):
        if dp[i][x] is None:
            continue
        # A[i]を倒すとき
        c = 2 if x else 1
        dp[i+1][x^1] = max(dp[i+1][x^1], dp[i][x]+c*A[i])
        # A[i]を倒さないとき
        dp[i+1][x] = max(dp[i+1][x], dp[i][x])

print(max(dp[N]))
