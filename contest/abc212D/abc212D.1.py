Q = int(input())
from heapq import heapify, heappop, heappush

hq = []
offset = 0
ans = []
for _ in range(Q):
    t, *X = map(int, input().split())
    if t == 1:
        heappush(hq, X[0] - offset)
    elif t == 2:
        offset += X[0]
    else:
        ans.append(offset + heappop(hq))

print(*ans, sep="\n")
