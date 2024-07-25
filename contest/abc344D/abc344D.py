T = input()
N = int(input())
S = [input().split()[1:] for _ in range(N)]
INF = 100000

from collections import defaultdict
dp = [defaultdict(lambda: INF) for _ in range(N+1)]
dp[0][""] = 0
# dp[i][s]: S[:i]まで見て、文字列sを作るときの最小金額

for i in range(N):
    for s in dp[i].keys():
        for t in S[i]:
            # print(T[len(s):len(s)+len(t)], t)
            dp[i+1][s] = min(dp[i+1][s], dp[i][s])
            if T[len(s):len(s)+len(t)]==t:
                ns = s+t
                dp[i+1][ns] = min(dp[i+1][ns], dp[i][s]+1)

# print(*dp, sep="\n")
print(dp[N][T] if dp[N][T]<INF else -1)
