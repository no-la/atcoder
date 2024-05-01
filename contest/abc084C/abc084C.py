N = int(input())
A = [list(map(int, input().split())) for _ in range(N-1)]


c = [0]*N # c[i]: 駅0からiまでにかかる時間
for i in range(1, N):
    c[i] = c[i-1] + A[i-1][0]
dp = [10**15]*N # dp[i]: 駅iからNに行くときの答え

