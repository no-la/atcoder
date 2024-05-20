N, X, Y = map(int, input().split())
A = list(map(int, input().split()))


ans = 0

ll, l, r, rr = -1, None, None, N # ll, rrは条件を満たさない
has_X = False
has_Y = False
for i in range(N):
    print(i, ll, l, r, rr, has_X, has_Y)
    if not has_X and not has_Y and A[i]<Y or A[i]>X:
        ll = i
    if has_X and has_Y and A[i]<Y or A[i]>X:
        rr = i
        ans += (l-ll)*(rr-r)
        
        has_X, has_Y = False, False
        
    if A[i]==X:
        has_X = True
        if not has_Y:
            l = i
        else:
            r = i
    if  A[i]==Y:
        has_Y = True
        if not has_X:
            l = i
        else:
            r = i

if has_X and has_Y:
    ans += (l-ll)*(rr-r)

print(ans)
