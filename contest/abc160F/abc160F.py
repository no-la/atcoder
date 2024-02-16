N = int(input())
from collections import defaultdict
d = defaultdict(list)
for _ in range(N):
    a, b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)


dp = [] # dp[i]: kから距離i以下の範囲での場合の数

