from collections import defaultdict
N, M = map(int, input().split())
UV = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split())
    UV[u].append(v)
    UV[v].append(u)

MOD = 998244353