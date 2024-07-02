N, M = map(int, input().split())

from heapq import heapify, heappop, heappush
from collections import defaultdict
events = []
d = defaultdict(list)
for _ in range(M):
    t, w, s = map(int, input().split())
    events.append(t)
    d[t].append((w, s))
heapify(events)

ans = [0]*N
A = list(range(N)) # 並んでいる人のりすと
heapify(A)
while events:
    t = heappop(events)
    for w, s in d[t][::-1]:
        if w==-1: # 人sが戻るイベント
            heappush(A, s)
        else: # 量wのそうめん
            if not A:
                continue
            p = heappop(A)
            ans[p] += w
            if t+s not in d:
                heappush(events, t+s)
            d[t+s].append((-1, p))
    
print(*ans, sep="\n")
            
