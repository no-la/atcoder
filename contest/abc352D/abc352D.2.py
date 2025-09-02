N, K = map(int, input().split())
P = list(map(int, input().split()))

A = [None] * (N + 1)
for i, p in enumerate(P):
    A[p] = i

from heapq import heapify, heappop, heappush

min_hq = []
max_hq = []

for i in range(1, K):
    heappush(min_hq, A[i])
    heappush(max_hq, -A[i])

ans = 1000000000
for a in range(1, N - K + 2):
    heappush(min_hq, A[a + K - 1])
    heappush(max_hq, -A[a + K - 1])

    while P[min_hq[0]] < a or P[min_hq[0]] >= a + K:
        heappop(min_hq)
    while P[-max_hq[0]] < a or P[-max_hq[0]] >= a + K:
        heappop(max_hq)

    # print(max_hq, min_hq)

    mx = -max_hq[0]
    mn = min_hq[0]
    ans = min(ans, mx - mn)

print(ans)
