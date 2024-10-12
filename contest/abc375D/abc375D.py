from collections import defaultdict

S = input()
N = len(S)

dp = [defaultdict(int) for _ in range(N + 1)]
# dp[i][s]: S[:i]まで調べてsになる場合の数

ans = 0
for i in range(N):
    dp[i + 1][S[i]] += 1
    for s in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        dp[i + 1][s] += dp[i][s]
        dp[i + 1][s + S[i]] += dp[i][s]
        for t in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            dp[i + 1][s + t] += dp[i][s + t]
            if s == S[i]:
                ans += dp[i][s + t]

print(ans)
