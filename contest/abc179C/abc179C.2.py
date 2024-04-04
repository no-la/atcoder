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
def prime_factors_num(n):
    """n(2<=n<=MAXN)の因数の個数を返す"""
    c = 0
    rev = 1
    pre = sieve[n]
    while n>1: # O(log n)
        if pre!=sieve[n]:
            rev *= c*(c+1)//2
            c = 0
        else:
            c += 1
            n //= sieve[n]
        pre = sieve[n]
        
        if ans[n] != 0:
            rev *= ans[n]
            break
    if c!=0:
            rev *= c+1
    return rev


ans = [0]*(N+1)
ans[1] = 1
for i in range(2, N):
    ans[i] = prime_factors_num(i)
print(sum(ans))
print(ans[:100])