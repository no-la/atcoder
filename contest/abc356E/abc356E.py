N = int(input())
A = list(map(int, input().split()))

A.sort()
d = [0]*(N+1) # d[i] = sum(A[:i])
for i in range(N+1):
    d[i] = d[i-1] + A[i-1]

ans = 0
for i in range(N):
    # お祈り
    ans += (d[-1]-d[i+1])
