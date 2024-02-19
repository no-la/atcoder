N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

import math

ans = 0
for i in range(N):
    for j in range(N):
        a, b = A[i], A[j]
        ans = max(ans, math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2))
print(ans)