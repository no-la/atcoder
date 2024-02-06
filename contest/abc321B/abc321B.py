N, X = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
s = sum(A[1:-1])
delta = X - s
ans = None
if delta > A[-1]:
    ans = -1
elif delta <= A[0]:
    ans = 0
else:
    ans = delta
print(ans)
