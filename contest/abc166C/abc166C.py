N, M = map(int, input().split())
H = list(map(int, input().split()))
from collections import defaultdict
d = defaultdict(list)
for _ in range(M):
    a, b = map(lambda x: int(x)-1, input().split())
    d[a].append(b)
    d[b].append(a)


ans = 0
#DFS
from collections import deque
dist = [-1]*N #todo[0]からの距離のリスト
for i in range(N):
    if dist[i]!=-1:
        continue
    todo = deque([i])
    dist[todo[0]] = 0
    maxh = H[i]
    while todo:
        v = todo.pop()
        good = True
        for w in d[v]:
            if H[v]<=H[w]:
                good = False
            if dist[w]!=-1: #既に調べた点は飛ばす
                continue
            todo.append(w)
            dist[w] = dist[v]+1
        if good:
            ans += 1

print(ans)