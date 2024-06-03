N = int(input())
A = list(map(int, input().split()))
M = max(A)

d = [0]*(M+1)
# d[v]: v==A[i]なるiの個数
for a in A:
    d[a] += 1

# osa_k法
MAXN = M+10
sieve = [i for i in range(MAXN)] # sieve[i]: iの最も小さい素因数
p = 2
while p*p<=MAXN: # O(MAXN * loglog MAXN)
    if sieve[p]==p:
        for q in range(p*p, MAXN, p):
            if sieve[q]==q:
                sieve[q] = p
    p += 1

# print(d)
ans = d[1]*d[1]*d[1]
for v in range(2, M+1):
    n = v
    seen = set()
    while n>1: # O(log n)
        if n not in seen:
            if n!=v//n:
                ans += d[v]*d[n]*d[v//n]*2
            else:
                ans += d[v]*d[n]*d[v//n]
            print(v, "=", n, "*", v//n, ans)
        seen.add(n)
        seen.add(v//n)
        n //= sieve[n]

print(ans)
