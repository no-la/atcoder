N = int(input())
A = list(map(int, input().split()))


# osa_k法
MAXN = 2*(10**5)+10
sieve = [i for i in range(MAXN)] # sieve[i]: iの最も小さい素因数
p = 2
while p*p<=MAXN: # O(MAXN * loglog MAXN)
    if sieve[p]==p:
        for q in range(p*p, MAXN, p):
            if sieve[q]==q:
                sieve[q] = p
    p += 1


from collections import defaultdict
d = defaultdict(int) # d[a]: Aの中にあるaの倍数の個数
for a in A: # O(N)
    fac = set()
    while a>1: # O(log a)
        d[a] += 1
        a //= sieve[a]

print([(a, d[a]) for a in A])
ans = sum([d[a]==1 for a in A])
print(ans)