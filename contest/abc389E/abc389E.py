N, M = map(int, input().split())
P = list(map(int, input().split()))
P.sort()

dp = [0] * (N + 1)
# dp[i]: P[:i]から選ぶときの最大個数
