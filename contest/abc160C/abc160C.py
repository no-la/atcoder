K, N = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
for i in range(N):
    A.append(A[i]+K)

ans = K
for i in range(N+1):
    ans = min(ans, A[i+N-1]-A[i])
print(ans)