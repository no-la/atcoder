import sys

input = lambda: sys.stdin.readline().rstrip()
N, K = map(int, input().split())
A = list(map(int, input().split()))
M = max(A)

# d[i]: 整数iがAの元の約数として何回現れるか, がつくれればいい？
# aの約数xのうち、d[x]>=Kなる最大のものが答え
# 10^6以下で最も約数が多い数字は？ -> 多分 2*3*5*7*11*13 で、約数は2^6=64個
# 違うわ。4*9*25*49=44100 は 3^4=81個
# 2^3*3*5*7*11*13=840840 は 2^7=128個
# 2^4*3^2*5*7*11*13=720720 は 5*3*2^4=240個
# まあ多分O(100)程度になる？


# osa_k法
MAXN = M + 10
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


divisors = [set([1]) for _ in range(M + 1)]
# divisors[a]: aの約数
count = [0] * (M + 1)
# count[x]: 約数としてxが現れる回数

for a in A:
    d = prime_factors(a) if a >= 2 else {1: 1}
    for k, v in d.items():
        pre = divisors[a].copy()
        for x in pre:
            for i in range(1, v + 1):
                divisors[a].add(x * (k**i))
