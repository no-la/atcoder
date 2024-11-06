Q = int(input())
from heapq import heapify, heappop, heappush

hq = []
heapify(hq)
offset = [0]
ans = []
for _ in range(Q):
    t, *X = map(int, input().split())
    if t == 1:
        heappush(hq, (X[0], len(offset) - 1))
    elif t == 2:
        offset.append(offset[-1] + X[0])
    else:
        x, i = heappop(hq)
        ans.append(offset[-1] - offset[i] + x)

print(*ans, sep="\n")
