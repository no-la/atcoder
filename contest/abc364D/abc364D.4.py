N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
M = 10**9

import bisect
for _ in range(Q):
    b, k = map(int, input().split())
    
    l, r = 0, M
    while l<r-1:
        c = (l+r)//2
        left = bisect.bisect_left(A, b-c)
        right = bisect.bisect_right(A, b+c)
        count = right-left
        if count>k:
            r = c
        else:
            l = c
    
    left = bisect.bisect_left(A, b-l)
    right = bisect.bisect_right(A, b+l)
    ans = max(abs(b-A[left]), abs(A[right-1]-b))
    print(ans)
