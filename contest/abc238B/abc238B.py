N = int(input())
A = list(map(int, input().split()))

for i in range(N-1):
    A[i+1] = (A[i+1]+A[i])%360

A.append(0)
A.append(360)
A.sort()

ans = 0
for i in range(N+1):
    temp = abs(A[i+1]-A[i])
    ans = max(ans, temp)
print(ans)