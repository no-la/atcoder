N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

import bisect
# 基本的にbisect_leftを使う
# 渡す配列は昇順(reverse=False)ソートしておく
for _ in range(Q):
    b, k = map(int, input().split())

    l, r = -1, 10**10
    while l<r-1:
        c = (l+r)//2
        left = bisect.bisect_left(A, b-c)
        right = bisect.bisect_right(A, b+c)
        count = right-left
        if count<k:
            l = c
        else:
            r = c
    print(l+1)
