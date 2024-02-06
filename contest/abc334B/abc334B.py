A, M, L, R = map(int, input().split())

if A<=L<=R:
    delta = (M - (L-A)%M)%M
    ans = (R-L-delta)//M+1
elif L<=A<=R:
    ans = (R-A)//M+(A-L)//M+1
else:
    delta = (M - (A-R)%M)%M
    ans = (R-L-delta)//M+1
print(ans)