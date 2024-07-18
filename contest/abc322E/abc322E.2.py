N, K, P = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

from collections import defaultdict
dp = [defaultdict(lambda:10**15) for _ in range(N+1)]
# dp[i][(a1, a2, ..., aK)]: A[:i]を使ってパラメータjをaj以上にするために必要な最小コスト

for i in range(N):
    dp[i][tuple([0]*K)] = 0
    for key in dp[i].keys():
        # print(key)
        nkey = []
        for j in range(K):
            nkey.append(min(P,  key[j]+A[i][j+1]))
        
        pkey = tuple(key)
        nkey = tuple(nkey)
        
        dp[i+1][nkey] = min(dp[i+1][nkey], dp[i][pkey]+A[i][0])
        dp[i+1][pkey] = min(dp[i+1][pkey], dp[i][pkey])


key = tuple([P]*K)
# for i in range(N+1):
#     print(dp[i].items(), "\n")
print(dp[N][key] if key in dp[N] else -1)