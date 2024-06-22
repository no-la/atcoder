N = int(input())
A = list(map(int, input().split()))

# A[i]-(b+(i+1)) = A[i]-(i+1) - b
for i in range(N):
    A[i] -= i+1

# A[i]-bを考えればいい
# ソートしていいのでは
A.sort()
d = [0]*(N+1) # d[i]: sum(A[:i])
for i in range(1, N+1):
    d[i] = d[i-1] + A[i-1]

# print(A)

# ... < A[i-1] < b = A[i] = ... = A[j-1] < A[j] < ...とすると
# sum([abs(a-b) for a in A])
# = ... + (b-A[i-1]) + (A[j]-b) + ...
# = i*b-sum(A[:i]) + sum(A[j:])-(N-j)*b
# = (i+j-N)*b + sum(A[j:]) - sum(A[:i])
# = (i+j-N)*b + sum(A) - sum(A[:j]) - sum(A[:i])
# = (i+j-N)*b + sum(A) - (j-i)*A[i] - 2*sum(A[:i])

ans = 10**15
i = 0
while i<N:
    j = i+1
    while j+1<N and A[j+1]==A[j]:
        j += 1
    b = A[i]
    ans = min(ans, (i+j-N)*b + d[N] - (j-i)*A[i] - 2*d[i])

    i = j+1

print(ans)
