N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()


import bisect
for _ in range(Q):
    b, k = map(int, input().split())
    bi = bisect.bisect_left(A, b)
    
    # 右側
    l, r = bi, N # b以上の要素としてA[l:r]を含む
    while l<r-1:
        c = (l+r)//2
        dist = A[c]-b
        
        left_i = bisect.bisect_left(A, b-dist)
        left_count = bi-left_i
        right_count = r-l
        count = left_count+right_count
        print(f"{b=}, {c=}, {left_count=}, {right_count=}")
        if count>k:
            r = c
        elif count==k:
            break
        else:
            l = c
    if count==k:
        print(dist)
        continue
    elif l<N:
        dist = A[l]-bi
        left_i = bisect.bisect_left(A, b-dist)
        left_count = bi-left_i
        right_count = r-l
        count = left_count+right_count
        if count==k:
            print(dist)
            continue

    print(l, r)
