N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()


import bisect
for _ in range(Q):
    b, k = map(int, input().split())
    bi = bisect.bisect_left(A, b)
    
    l, r = bi, N # b以上の要素はA[l:r]を含む
    while l<r-1:
        c = (l+r)//2
        dist = A[c]-b
        
        left_i = bisect.bisect_left(A, b-dist)
        left_count = bi-left_i
        right_count = r-l
        count = left_count+right_count
        if count>k:
            r = c
        elif count==k:
            break
        else:
            l = c
    if count==k:
        print(dist)
        continue
    # print(l, r)
    l, r = -1, bi # b以下の要素はA[l+1:r+1]を含む
    while l<r-1:
        c = (l+r)//2
        dist = b-A[c]
        
        left_i = bisect.bisect_left(A, b+dist)
        left_count = bi-left_i
        right_count = r-l
        count = left_count+right_count
        if count>k:
            l = c
        elif count==k:
            break
        else:
            r = c
    print(dist)
