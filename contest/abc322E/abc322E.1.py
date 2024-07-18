N, K, P = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

from collections import defaultdict
dp = [defaultdict(lambda:10**15) for _ in range(N+1)]
# dp[i][(a1, a2, ..., aK)]: A[:i]を使ってパラメータjをaj以上にするために必要な最小コスト
dp[0] = defaultdict(int)
for i in range(1, N+1):
    dp[i][tuple([0]*K)] = 0

import itertools
for i in range(1, N+1):
    # 重複あり組み合わせ O(nHk)=O(n+k-1Ck)
    for key in itertools.combinations_with_replacement(list(range(P+1)), K):
        # print(key)
        pre_key = []
        for j in range(K):
            pre_key.append(max(0,  key[j]-A[i-1][j+1]))
        
        pre_key = tuple(pre_key)
        if pre_key not in dp[i-1]:
            continue
        
        dp[i][tuple(key)] = min(dp[i][tuple(key)], A[i-1][0] + dp[i-1][tuple(pre_key)], dp[i-1][tuple(key)])


key = tuple([P]*K)
for i in range(N+1):
    print(dp[i].items(), "\n")
print(dp[N][key] if key in dp[N] else -1)