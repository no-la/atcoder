N = int(input())
A = list(map(int, input().split()))

B = [(A[i], i) for i in range(N)]
B.sort()

d = [0]*N
for i in range(N):
    d[B[i][1]] = i+1

ans = 0
for i in range(N):
    ans += A[i]*(d[i]-1 - (N-d[i]))

print(ans)
