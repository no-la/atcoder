import math

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

cumsum = [0] * MAXN
# cumsum[i]: i以下の素数の個数
for i in range(2, MAXN):
    cumsum[i] = cumsum[i - 1] + (sieve[i] == i)

ans = 0
for a in range(2, 1000):
    if a**5 > N:
        break
    if sieve[a] < a:
        continue
    for b in range(a + 1, 10000):
        if a * a * (b**3) > N:
            break
        if sieve[b] < b:
            continue

        c_max = int(math.sqrt(N // (a * a * b)))
        # print(a, b, c_max)
        ans += max(0, cumsum[min(MAXN - 1, c_max)] - cumsum[b])

# print(cumsum)
print(ans)
