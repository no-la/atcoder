
N = map(int, input().split())
A = list(map(int, input().split()))

# osa_k法
MAXN = 10**5+10
sieve = [i for i in range(MAXN)] # sieve[i]: iの最も小さい素因数
p = 2
while p*p<=MAXN: # O(MAXN * loglog MAXN)
    if sieve[p]==p:
        for q in range(p*p, MAXN, p):
            if sieve[q]==q:
                sieve[q] = p
    p += 1

from collections import defaultdict
def gcd_count(n):
    """n(2<=n<=MAXN)の素因数を返す"""
    d = defaultdict(int) # 適宜変更
    while n>1: # O(log n)
        d[sieve[n]] += 1
        n //= sieve[n]
    rev = 1
    for v in d.values():
        rev *= v+1
    return rev

d = [gcd_count(a) for a in A]

from functools import cache
#メモ化再帰
turn = 0
@cache
def f(n):
    # nから始めて、先手が勝つかどうか
    if n==1:
        return turn%2==0
    
    