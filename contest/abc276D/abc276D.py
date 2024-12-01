import math
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))


def prime_factors(n):
    t = n
    rev = defaultdict(int)
    for i in range(2, n):
        if i**2 > n:
            break
        while t % i == 0:
            t //= i
            rev[i] += 1
    if t != 1:
        rev[t] += 1
    # print(n, "->", rev)
    return rev


t = math.gcd(*A)

ans = 0
for i in range(N):
    a = A[i]
    tar = a // t
    if tar == 1:
        continue

    d = prime_factors(tar)
    if set(d.keys()) <= set([2, 3]):
        ans += d[2] + d[3]
    else:
        print(-1)
        exit()

print(ans)
