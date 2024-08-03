N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

ans = 0
cs = 0
for i in range(N):
    cs += A[i]
    temp = cs + A[i]*(N-i-1)
    if temp<=M:
        ans = A[i]
        # print(i, cs, "+", A[i], "x", N-i-1, "=", temp)
    else:
        l, r = A[i-1], A[i]

        while l<r-1:
            c = (l+r)//2
            temp = cs + c*(N-i-1)
            if temp>M:
                r = c
            else:
                l = c
        
        ans = l
        break
    
print(ans if ans<A[-1] else "infinite")
