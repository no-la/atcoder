N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

print(A)
import bisect
for _ in range(Q):
    b, k = map(int, input().split())
    bi = bisect.bisect_left(A, b)
    
    l, r = 0, N # b以上の要素はA[l:r]を含む
    while l<r-1:
        c = (l+r)//2
        dist = A[c]-b
        
        c_count = abs(c-bi)
        other_i = bisect.bisect_left(A, b-dist)
        other_count = abs(bi-other_i)
        count = c_count+other_count
        if count>k:
            r = c
        elif count==k:
            break
        else:
            l = c
    
    print(abs(b-A[c]))
    print(f"{b=}, {k=}, {l=}, {r=}, {other_count=}, {other_i=}, {c_count=}, {dist=}")
