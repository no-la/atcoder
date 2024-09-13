N = int(input())
A = list(map(int, input().split()))

dp = [0]*N
# dp[i]: マスiに到達するまでにサイコロを振る回数の期待値

