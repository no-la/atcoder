N, M, K = map(int, input().split())
from collections import defaultdict
A = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    A[a].append(b)
    A[b].append(a)

# 各点に到達するときの警備員の残り体力のlistを作ればいい
d = [-1]*N

from heapq import heapify, heappop, heappush
#heapify(a:list)
#heappop(a) (最小値)
#heappush(a, value)
todo = []
heapify(todo)
for _ in range(K):
    p, h = map(int, input().split())
    p -= 1
    d[p] = h
    heappush(todo, (-h, p))

while todo:
    vh, v = heappop(todo)
    wh = -vh - 1
    for w in A[v]:
        if d[w]>=wh: # 既に調べた点は飛ばす
            continue
        d[w] = wh
        heappush(todo, (-wh, w))

ans = [i+1 for i in range(N) if d[i]>=0]
print(len(ans))
print(*ans)
