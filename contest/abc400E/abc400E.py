import sys

input = lambda: sys.stdin.readline().rstrip()
Q = int(input())
M = 10**12


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


targets = []

for i in range(6, M):
    if i**2 > M:
        break
    d = prime_factors(i)
    if len(d) == 2:
        targets.append(i**2)

import bisect

# print(targets)
for _ in range(Q):
    A = int(input())
    print(targets[bisect.bisect_right(targets, A) - 1])
