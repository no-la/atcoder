N = int(input())

# osa_k法
MAXN = N+10
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
    d = defaultdict(int) # 適宜変更
    while n>1: # O(log n)
        d[sieve[n]] += 1
        n //= sieve[n]
    return d

ans = 1
i = 2
while i**2<=N:
    d = prime_factors(i**2)
    temp = 1
    for v in d.values():
        temp *= v+1
    print(i**2, d.items(), temp)
    ans += temp
    i += 1

print(ans)
