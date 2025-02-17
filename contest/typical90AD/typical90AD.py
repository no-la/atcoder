import sys

input = lambda: sys.stdin.readline().rstrip()
N, K = map(int, input().split())


MAXN = N + 1
sieve = [i for i in range(MAXN)]  # sieve[i]: iの最も小さい素因数
count = [0] * MAXN
count[1] = 1
p = 2
while p * p <= MAXN:  # O(MAXN * log MAXN)
    if sieve[p] == p:
        for q in range(p, MAXN, p):
            if sieve[q] == q:
                sieve[q] = p
            count[q] += 1
    p += 1


ans = sum([c >= K for c in count])

print(ans)


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

from collections import defaultdict


def prime_factors(n):
    """n(2<=n<=MAXN)の素因数を返す"""
    d = defaultdict(int)  # 適宜変更
    while n > 1:  # O(log n)
        d[sieve[n]] += 1
        n //= sieve[n]
    return d
