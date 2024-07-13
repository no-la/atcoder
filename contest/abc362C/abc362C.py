N = int(input())
L = []
R = []
for _ in range(N):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

SL = sum(L)
SR = sum(R)

X = []
s = 0
for i in range(N):
    l, r = L[i], R[i]+1
    while l<r-1:
        c = (l+r)//2
        if SL-L[i]+c>0:
            r = c
        
        
        
    c = (l+r)//2
    SL = SL-L[i]+c
    SR = SR-R[i]+c
    X.append(c)

if sum(X)==0:
    print("Yes")
    print(*X)
else:
    print("No")
    print(*X)
