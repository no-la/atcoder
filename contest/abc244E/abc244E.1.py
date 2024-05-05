
# https://atcoder.jp/contests/abc244/submissions/53169330
N, M, K, S, T, X = map(int, input().split())
from collections import defaultdict
d = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split())
    d[u].append(v)
    d[v].append(u)
MOD = 998244353

dp = [[[0, 0] for __ in range(N+1)] for _ in range(K+1)]
# dp[i][j][k]: Xを偶数(k=0) or 奇数(k=1)回、かつ辺をi個通ってjに行く場合の数
dp[0][S][0] = 1

for i in range(1, K+1):
    for j in range(1, N+1): # 辺がM個なので、これ以下のループは合計でMになる
        temp = 0
        for w in d[j]:
            if j!=X:
                dp[i][j][0] = (dp[i][j][0] + dp[i-1][w][0])%MOD
                dp[i][j][1] = (dp[i][j][1] + dp[i-1][w][1])%MOD
            else:
                dp[i][j][0] = (dp[i][j][0] + dp[i-1][w][1])%MOD
                dp[i][j][1] = (dp[i][j][1] + dp[i-1][w][0])%MOD
                

# print(*dp, sep="\n")
print(dp[K][T][0])

