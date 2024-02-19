N, M, K = map(int, input().split())

import math
g = math.lcm(N, M)

a = g//N+g//M-2

if K%a==0:
    print(g*(K//a)-min(N, M))
    exit()

ni, mi = 0, 0
while ni+mi<K%a:
    if N*(ni+1)<=M*(mi+1):
        ni += 1
    else:
        mi += 1
print(g*(K//a)+max(N*ni, M*mi))