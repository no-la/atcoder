"""https://prd-xxx.hateblo.jp/entry/2020/08/30/163140"""

# エラトステネスの篩の強化版
MAXN = 10**6+10
sieve = [i for i in range(MAXN)] # sieve[i]: iの最も小さい素因数
p = 2
while p*p<=MAXN:
    if sieve[p]==p:
        for q in range(p*p, MAXN, p):
            if sieve[q]==q:
                sieve[q] = p
    p += 1

from collections import defaultdict
def prime_factors(n):
    """nの素因数を返す"""
    d = defaultdict(int)
    while n>1:
        d[sieve[n]] += 1
        n //= sieve[n]
    return d
        


if __name__ == '__main__':
    for i in range(2, 30):
        print(prime_factors(i))