N, M = map(int, input().split())
A = list(map(int, input().split()))

import bisect

A.sort()
for i in range(N):
    print(bisect.bisect_left(A, -(i + 1)))
