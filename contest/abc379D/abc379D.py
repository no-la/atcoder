Q = int(input())

offset = 0
from heapq import heapify, heappop, heappush

hq = []
for _ in range(Q):
    i, *x = map(int, input().split())
    # print(hq, offset)
    if i == 1:
        heappush(hq, offset)
    elif i == 2:
        T = x[0]
        offset += T
    else:
        H = x[0]
        ans = 0
        while hq and -hq[0] + offset >= H:
            heappop(hq)
            ans += 1
        print(ans)
