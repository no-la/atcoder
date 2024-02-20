N, M = map(int, input().split())
A = list(map(int, input().split()))

border = sum(A)/(4*M)
ans = 0
for i in range(N):
    if A[i]>=border:
        ans += 1
print("Yes" if ans>=M else "No")