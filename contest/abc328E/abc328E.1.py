N, M, K = map(int, input().split())
E = []
for _ in range(M):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    E.append((u, v, w))

# 全域木はなん通りある？
# 全域木はN-1辺なので、最大でMC(N-1)通り
# 28C8 ~ 3*10^6

import itertools
from collections import deque

ans = 10**16
for l in itertools.combinations(range(M), N - 1):
    temp = 0
    d = [[] for _ in range(N)]
    for i in l:
        u, v, w = E[i]
        d[u].append(v)
        d[v].append(u)
        temp += w
        temp %= K

    # 全域木かどうか調べる
    # 辺の個数をN-1にしているので連結であれば木
    # DFS
    todo = deque([0])
    seen = set([0])
    while todo:
        v = todo.pop()
        for w in d[v]:
            if w in seen:  # 既に調べた点は飛ばす
                continue
            todo.append(w)
            seen.add(w)
    if len(seen) == N:
        ans = min(ans, temp)

print(ans)
