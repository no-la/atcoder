N, M = map(int, input().split())
INF = -1
from collections import defaultdict
d = defaultdict(list)
for i in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    d[a].append((c, b, i))
    d[b].append((c, a, i))

# 点0から各点への最短ルートに使われる辺をあつめればいい
from heapq import heapify, heappop, heappush
#heapify(a:list)
#heappop(a) (最小値)
#heappush(a, value)


todo = d[0]
heapify(todo)
used = [False]*M
visited = [False]*N
dist = [INF]*N

dist[0] = 0
for c, a, i in d[0]:
    dist[a] = c

while todo:
    # print(todo)
    vc, va, vi = heappop(todo)
    if visited[va]:
        continue
    visited[va] = True
    used[vi] = True
    for wc, wa, wi in d[va]:
        if dist[wa]==INF or dist[wa]>dist[va]+wc:
            used[vi] = True
            dist[wa] = dist[va]+wc
            heappush(todo, (dist[wa], wa, wi))

ans = []
for i in range(M):
    if used[i]:
        ans.append(i+1)

# print("dist", "-"*20, dist, sep="\n")
# print("used", "-"*20, used, sep="\n")
print(*ans)
