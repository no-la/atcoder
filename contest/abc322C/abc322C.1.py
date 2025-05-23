N, M = map(int, input().split())
A = list(map(int, input().split()))

import bisect

for i in range(1, N + 1):
    t = bisect.bisect_left(A, i)
    print(A[t] - i)
