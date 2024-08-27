
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
def f(n):
    """n(2<=n<=MAXN)の素因数を返す"""
    if n==1:
        return 0
    d = defaultdict(int) # 適宜変更
    while n>1: # O(log n)
        d[sieve[n]] += 1
        n //= sieve[n]
    return sum(d.values())

d = [f(a) for a in A]
# d[_] <= log(10^5) < 20

ans = 0
for i in d:
    ans ^= i
# print(d)
print("Anna" if ans else "Bruno")    
    