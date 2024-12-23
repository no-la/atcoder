N = int(input())
d = [[] for _ in range(N)]
deg = [0] * N
for _ in range(N - 1):
    u, v = map(lambda x: int(x) - 1, input().split())
    d[u].append(v)
    d[v].append(u)
    deg[u] += 1
    deg[v] += 1

from collections import defaultdict

ans = N
# 赤の全探索
for i in range(N):
    leaf = defaultdict(int)
    # leaf[k]: k個の葉を持つ頂点の個数
    for j in d[i]:
        if deg[j] == 1:
            continue
        leaf[deg[j] - 1] += 1
    ks = list(leaf.keys())
    ks.sort()
    cumsum = [0] * (len(ks) + 1)
    for j, k in enumerate(ks):
        cumsum[j + 1] = cumsum[j] + leaf[k]
    for j, y in enumerate(ks):
        # 葉の個数をyにするとき
        x = cumsum[-1] - cumsum[j]
        ans = min(ans, N - (x * y + x + 1))

print(ans)
