N = int(input())
INF = N


tar = [1]
for a in [6, 9]:
    for i in range(1, 100000):
        if a**i > N:
            break
        tar.append(a**i)
tar.sort()

dp = [INF] * (N + 1)
# dp[i]: i円を作るための最小コスト
dp[0] = 0
for i in range(N):
    for t in tar:
        if i + t > N:
            break
        dp[i + t] = min(dp[i + t], dp[i] + 1)

print(dp[N])
