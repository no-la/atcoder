N = int(input())
A = list(map(int, input().split()))

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
    d = defaultdict(int) # 適宜変更
    while n>1: # O(log n)
        d[sieve[n]] += 1
        n //= sieve[n]
    return d

is_setwise_coprime = True
is_pairwise_coprime = True
count = [0]*MAXN
for a in A:
    l = prime_factors(a)
    for i in l.keys():
        count[i] += 1

is_setwise_coprime = all([c<N for c in count])
is_pairwise_coprime = all([c<2 for c in count])

if is_pairwise_coprime:
    print("pairwise coprime")
elif is_setwise_coprime:
    print("setwise coprime")
else:
    print("not coprime")
