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
for i in range(N):
    if i<N-1:
        x = max(L[i], R[i]-SR)
        if not (x<=R[i] and x<=L[i]-SL):
            print("No")
            exit()
        
        X.append(x)
        SR = SR-R[i]+x
        SL = SL-L[i]+x
    else:
        x = -sum(X)
        if not (L[i]<=x<=R[i]):
            print("No")
            exit()
        X.append(x)

print("Yes")
print(*X)
