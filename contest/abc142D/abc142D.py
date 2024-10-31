A, B = map(int, input().split())

import math

gcd = math.gcd(A, B)

if gcd == 1:
    print(1)
    exit()

# osa_k法
MAXN = 10**6 + 10
sieve = [i for i in range(MAXN)]  # sieve[i]: iの最も小さい素因数
p = 2
while p * p <= MAXN:  # O(MAXN * loglog MAXN)
    if sieve[p] == p:
        for q in range(p * p, MAXN, p):
            if sieve[q] == q:
                sieve[q] = p
    p += 1

ans = 1
n = 1
for i in range(2, gcd + 1):
    if i**2 > gcd:
        break
    if sieve[i] == i and gcd % i == 0:
        ans += 1
        while gcd % (n * i) == 0:
            n *= i

if (gcd // n) ** 2 > gcd:
    ans += 1

print(ans)
