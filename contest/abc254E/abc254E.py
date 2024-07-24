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
    todo = deque([x])
    dist = [-1]*N #todo[0]からの距離のリスト
    dist[todo[0]] = 0
    ans = x+1
    while todo:
        v = todo.popleft()
        ndist = dist[v] + 1
        for w in d[v]:
            if dist[w]!=-1: # 既に調べた点は飛ばす
                continue
            if ndist<k:
                todo.append(w)
            if ndist<=k:
                dist[w] = ndist
                ans += w+1
    # print(x+1, dist)
    print(ans)

