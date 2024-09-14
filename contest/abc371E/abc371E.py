N = int(input())
A = list(map(int, input().split()))

import math
ans = 0
d = [-1]*(N+1)
for i in range(N):
    a = A[i]
    ans += (N-i)*(i-d[a])
    # print(i, ans)
    
    d[a] = i

print(ans)
