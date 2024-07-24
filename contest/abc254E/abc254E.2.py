N, M = map(int, input().split())
from collections import defaultdict
d = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    d[a].append(b)
    d[b].append(a)
Q = int(input())

from collections import deque
for _ in range(Q):
    x, k = map(int, input().split())
    x -= 1
    # BFS
    todo = deque([(x, 0)])
    seen = set([x])
    ans = x+1
    while todo:
        v, vd = todo.popleft()
        wd = vd + 1
        for w in d[v]:
            if w in seen: # 既に調べた点は飛ばす
                continue
            seen.add(w)
            if wd<k:
                todo.append((w, wd))
            if wd<=k:
                ans += w+1
    # print(x+1, dist)
    print(ans)

