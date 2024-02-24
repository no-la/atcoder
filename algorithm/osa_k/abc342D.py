"""https://atcoder.jp/contests/abc342/submissions/50618135"""
import math
from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))

# osa_k法
MAXN = 2*10**5+10
sieve = [i for i in range(MAXN)] # sieve[i]: iの最も小さい素因数
p = 2
while p*p<=MAXN: # O(MAXN * loglog MAXN)
    if sieve[p]==p:
        for q in range(p*p, MAXN, p):
            if sieve[q]==q:
                sieve[q] = p
    p += 1

def prime_factors(n):
    """n(2<=n<=MAXN)の素因数を返す"""
    d = defaultdict(int) # 適宜変更
    while n>1: # O(log n)
        d[sieve[n]] += 1
        n //= sieve[n]
    return d


d = defaultdict(int)

zeros = 0
# O(N*log N)
for a in A:
    if a==0: # 0は別
        zeros += 1
        continue
    
    pf = prime_factors(a) # O(log a)
    v = math.prod([k for k, v in pf.items() if v%2==1] + [1]) # O(log a)
    d[v] += 1

# [0, 0以外], [0, 0], その他
print(zeros*(N-zeros) + zeros*(zeros-1)//2
      + sum([v*(v-1)//2 for v in d.values()]))
    