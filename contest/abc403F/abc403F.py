"""途中まで"""

import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
INF = 10**18

# osa_k法
MAXN = N
sieve = [i for i in range(MAXN)]  # sieve[i]: iの最も小さい素因数
p = 2
while p * p <= MAXN:  # O(MAXN * loglog MAXN)
    if sieve[p] == p:
        for q in range(p * p, MAXN, p):
            if sieve[q] == q:
                sieve[q] = p
    p += 1

from collections import defaultdict


def prime_factors(n):
    """n(2<=n<=MAXN)の素因数を返す"""
    d = defaultdict(int)  # 適宜変更
    while n > 1:  # O(log n)
        d[sieve[n]] += 1
        n //= sieve[n]
    return d


dp = [[INF] * 2 for _ in range(N + 1)]
dp[1] = [1, 1]
# dp[i][j]: iを作り、一番外側の演算が+(j=0), * (j=1) のときの最小値

for i in range(2, N + 1):
    # 和
    for j in range(1, i // 2 + 1):
        dp[i][0] = min(dp[i], dp[j] + dp[i - j] + 1)

    # 積
    fac = prime_factors(i).keys()
    for x in fac:
        dp[i] = min(dp[i], dp[x] + dp[i // x])
