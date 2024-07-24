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

count = [0]*(1+N) # 平方数としてあふれてる部分をkeyとして数える
count[1] = 1
for i in range(2, N+1):
    d = prime_factors(i)
    temp = 1
    for k, v in d.items():
        temp *= k**(v%2)
    count[temp] += 1

ans = 0
for i in range(1, N+1):
    d = prime_factors(i)
    temp = 1
    for k, v in d.items():
        temp *= k**(v%2)
    ans += count[temp]
# print(count)
print(ans)
