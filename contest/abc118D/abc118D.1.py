N, M = map(int, input().split())
A = list(map(int, input().split()))
D = [None,2,5,5,4,5,6,3,7,6] # D[i]: 数字iを作るために必要なマッチの数

dp = [None]*(N+1) # dp[i]: ちょうどi本使うときの最大の数
dp[0] = 0
for i in range(1, N+1):
    for a in A:
        if i-D[a]>=0 and dp[i-D[a]]!=None:
            dp[i] = max(dp[i] if dp[i] else 0, dp[i-D[a]]*10+a)
print(dp[N])