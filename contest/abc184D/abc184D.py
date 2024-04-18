A, B, C = map(int, input().split())

dp = [[[0]*101 for _ in range(101)] for _ in range(101)]
# dp[i][j][k]: 金貨がi枚、銀貨がj枚、銅貨がk枚ある確率

cs = [[0]*102 for _ in range(3)]
# cs[_][i]: 各硬貨がi枚ある確率


