"""NS"""

from collections import defaultdict

N, M = map(int, input().split())
after = defaultdict(list)
before = defaultdict(list)
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    after[a].append((b, c))
    before[b].append((a, c))
INF = 10**10

dp = [[[INF] * N for _ in range(N)] for _ in range(N)]
# dp[k][s][t]: f(s, t, k)

for k in range(N):
    for i in range(k + 1):
        dp[k][i][i] = 0
for i in range(N):
    for j, c in after[i]:
        for k in range(N):
            dp[k][i][j] = c

for k in range(N):  # kを通れるようになる
    for i in range(1, k + 1):
        dp[k][i][i] = 0
    for i, ic in before[k]:
        for j, jc in after[k]:
            dp[k][i][k] = ic
            dp[k][k][j] = jc
            for s in range(k + 1):
                for t in range(k + 1):
                    dp[k][s][k] = min(dp[k][s][k], dp[k - 1][s][i] + dp[k][i][k])
                    dp[k][k][t] = min(dp[k][k][t], dp[k][k][j] + dp[k - 1][j][t])
                    dp[k][s][t] = min(
                        dp[k][s][t], dp[k - 1][s][t], dp[k][s][k] + dp[k][k][t]
                    )

print(*dp, sep="\n")
ans = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            dp[k][i][j] = dp[k][i][j] if dp[k][i][j] < INF else 0
            ans += dp[k][i][j]

print(ans)
