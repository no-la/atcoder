N = int(input())
# qで全探索

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

d = [0]*MAXN
for p in range(2, MAXN):
    d[p] = d[p-1] + (sieve[p]==p)

ans = 0
for q in range(2, MAXN):
    if q**3 > N:
        break
    if sieve[q]==q:
        maxp = min(q-1, N//(q**3))
        ans += d[maxp]

print(ans)
