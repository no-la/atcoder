import sys, math

input = lambda: sys.stdin.readline().rstrip()
T = int(input())
P = []  # 素数のlist
# osa_k法
MAXN = 3 * 10**6 + 1
sieve = [i for i in range(MAXN)]  # sieve[i]: iの最も小さい素因数
p = 2
while p * p <= MAXN:  # O(MAXN * loglog MAXN)
    if sieve[p] == p:
        for q in range(p * p, MAXN, p):
            if sieve[q] == q:
                sieve[q] = p
    p += 1

for i in range(2, MAXN):
    if sieve[i] == i:
        P.append(i)

for _ in range(T):
    N = int(input())
    for p in P:
        if N % p == 0:
            if N % (p**2) == 0:
                a, b = p, N // (p**2)
            else:
                a, b = int(math.sqrt(N // p)), p

            print(a, b)
            break
