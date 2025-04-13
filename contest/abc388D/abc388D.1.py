import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
A = list(map(int, input().split()))

from heapq import heapify, heappop, heappush

until = []
ans = [0] * N
for i in range(N):
    while until and i > until[0]:
        heappop(until)

    A[i] += len(until)
    use = min(N - i - 1, A[i])
    ans[i] = A[i] - use
    heappush(until, i + use)

print(*ans)
