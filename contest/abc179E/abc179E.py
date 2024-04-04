N, X, M = map(int, input().split())

import math
a = 0
now = X
ans = 0
i = 0
while i**2<=N:
    ans += now
    now = pow(now, 2, M)
print(ans)