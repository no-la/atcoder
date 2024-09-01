H, W, N = map(int, input().split())
A = [list(map(lambda x: int(x)-1, input().split()))]
A.sort()

dp = [0]*(N+1) # dp[i][x]: A[i]を取る(x=1)または取らない(x=0)ときの最大値
before = []
