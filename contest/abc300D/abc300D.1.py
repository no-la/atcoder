N = int(input())
# a^5 <= N
# a < 10^3

# osa_k法
MAXN = 10**6 + 10
sieve = [i for i in range(MAXN)]  # sieve[i]: iの最も小さい素因数
p = 2
while p * p <= MAXN:  # O(MAXN * loglog MAXN)
    if sieve[p] == p:
        for q in range(p * p, MAXN, p):
            if sieve[q] == q:
                sieve[q] = p
    p += 1


P = [i for i in range(2, MAXN) if sieve[i] == i]
# print(P)

M = len(P)
ans = 0
for i in range(M):
    for j in range(i + 1, M):
        for k in range(j + 1, M):
            ans += (P[i] ** 2) * P[j] * (P[k] ** 2) <= N

print(ans)
