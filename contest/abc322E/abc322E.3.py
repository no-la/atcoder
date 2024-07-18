N, K, P = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
INF = 10**15

from collections import defaultdict
dp = [defaultdict(lambda:INF) for _ in range(N+1)]
# dp[i][(a1, a2, ..., aK)]: A[:i]を使ってパラメータjをaj以上にするために必要な最小コスト
dp[0][tuple([0]*K)] = 0

import itertools
for i in range(1, N+1):
    # 重複あり組み合わせ O(nHk)=O(n+k-1Ck)
    for key in itertools.product(*[list(range(P+1))]*K):
        # print(key)
        pkey = []
        for j in range(K):
            pkey.append(max(0,  key[j]-A[i-1][j+1]))
        
        nkey = tuple(key)
        pkey = tuple(pkey)
        dp[i][nkey] = min(dp[i][nkey], dp[i-1][pkey]+A[i-1][0], dp[i-1][nkey])
        # if dp[i][nkey]<INF:
        #     print(i, pkey, "to", nkey, "by", A[i-1])


key = tuple([P]*K)
# for i in range(N+1):
#     print(*list(map(lambda x: f"{x[0]} -> {x[1]}" if x[1]<INF else "", dp[i].items())), "\n")
print(dp[N][key] if dp[N][key]<INF else -1)