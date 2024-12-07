N = int(input())

# x^2*y^2 or z^8
# 全探索できそう？
M = 10**7

MAXN = M
sieve = [i for i in range(MAXN)]  # sieve[i]: iの最も小さい素因数
p = 2
while p * p <= MAXN:  # O(MAXN * loglog MAXN)
    if sieve[p] == p:
        for q in range(p * p, MAXN, p):
            if sieve[q] == q:
                sieve[q] = p
    p += 1

import bisect

ans = 0

d = []
for i in range(2, M):
    if i**2 > N:
        break
    if sieve[i] != i:
        continue
    d.append(i**2)

# a^2 * b^2
for i, x in enumerate(d):
    j = bisect.bisect_right(d, int(N / x))
    if i >= j - 1:  # x<yとする
        break
    # print(x, d[j - 1])
    ans += j - i - 1


# z^8
for z in range(2, M):
    if sieve[z] != z:
        continue
    if z**8 <= N:
        ans += 1
    else:
        break


print(ans)
