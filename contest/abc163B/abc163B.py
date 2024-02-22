N, M = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
count = 0
for i in range(M):
    count += A[i]
    if count>N:
        count = N+1
        break
print(N-count)