N = int(input())

# 0, 1, ..., N-1の約数の個数

# osa_k法
MAXN = 10**6+10
sieve = [i for i in range(MAXN)] # sieve[i]: iの最も小さい素因数
p = 2
while p*p<=MAXN: # O(MAXN * loglog MAXN)
    if sieve[p]==p:
        for q in range(p*p, MAXN, p):
            if sieve[q]==q:
                sieve[q] = p
    p += 1

from collections import defaultdict
def prime_factors(n):
    """n(2<=n<=MAXN)の素因数を返す"""
    rev = 1
    while n>1: # O(log n)
        p = sieve[n]
        c = 1
        while n%p==0:
            n //= sieve[n]
            c += 1
        rev *= c
    return rev


ans = 1
for i in range(2, N):
    ans += prime_factors(i)
print(ans)