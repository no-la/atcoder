# エラトステネスの篩の強化版
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
    """n(>=2)の素因数を返す"""
    d = defaultdict(int) # 適宜変更
    while n>1: # O(log n)
        d[sieve[n]] += 1
        n //= sieve[n]
    return d

if __name__ == '__main__':
    for i in range(2, 31):
        print(i, prime_factors(i))