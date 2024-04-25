N = int(input())
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

e = [0]*(N+1)
ans = []

from collections import defaultdict
def prime_factors(n):
    """n(2<=n<=MAXN)の素因数を返す"""
    d = defaultdict(int) # 適宜変更
    while True: # O(log n)
        e[n**(d[n])] += 1
        e[n**(d[n])] %= 2
        if n==1:
            break
            
        d[sieve[n]] += 1
        n //= sieve[n]


for i in range(N, 0, -1):
    if e[i]==A[i-1]:
        continue
    else:
        ans.append(i)
        e[i] %= 2
        prime_factors(i)    

print(len(ans))
if ans:
    print(*ans)
