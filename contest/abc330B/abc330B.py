N, L, R = map(int, input().split())
A = list(map(int, input().split()))

ans = []
for i in range(N):
    if L<A[i]<R:
        d = min(abs(L-A[i]), abs(R-A[i]))
        if abs(L-A[i])<=abs(R-A[i]):
            ans.append(L+d)
        else:
            ans.append(R-d)
    else:
        if abs(L-A[i])<=abs(R-A[i]):
            ans.append(L)
        else:
            ans.append(R)
print(" ".join(map(str, ans)))