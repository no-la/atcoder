N = int(input())
A = list(map(int, input().split()))

dp = [[0]*(N+1) for _ in range(2)]
# dp[i]: 動物1からiに餌をあげるための費用の最小値



