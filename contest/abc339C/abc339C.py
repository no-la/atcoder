N = int(input())
A = list(map(int, input().split()))

now = 0
minv = 0
for i in range(N):
    now += A[i]
    minv = min(minv, now)

if minv>=0:
    print(now)
else:
    print(now-minv)