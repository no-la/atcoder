N = int(input())
A = list(map(int, input().split()))
M = 2**N

from collections import defaultdict

dp = [defaultdict(lambda: False) for _ in range(N + 1)]
# dp[i][j]: A[:i]からjを作れるか
dp[1][A[0]] = True

for i in range(1, N):
    for j in dp[i].keys():
        if not dp[i][j]:
            continue
        dp[i + 1][j] = True
        dp[i + 1][j ^ A[i]] = True

print(*dp, sep="\n")
print(sum(dp[N].values()))
