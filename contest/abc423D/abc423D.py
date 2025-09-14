import sys

input = lambda: sys.stdin.readline().rstrip()
N, K = map(int, input().split())

from heapq import heapify, heappop, heappush
from collections import deque

q = []
mati = deque()
tabe = 0
ans = []

for _i in range(N + 1):
    if _i == N:
        a = 10**18
    else:
        a, b, c = map(int, input().split())

    while q and q[0][0] <= a:
        t, v = heappop(q)
        tabe -= v

        while mati and tabe + mati[0][1] <= K:
            s, w = mati.popleft()
            tabe += w
            heappush(q, (t + s, w))
            ans.append(t)
            # print(t, q, mati)

    if _i == N:
        break

    if (not mati) and tabe + c <= K:
        tabe += c
        heappush(q, (a + b, c))
        ans.append(a)
    else:
        mati.append((b, c))

print(*ans, sep="\n")
