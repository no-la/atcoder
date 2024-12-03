N = int(input())
MOD = 998244353
M = 6

from functools import cache
import sys

sys.setrecursionlimit(10**7)


# メモ化再帰
@cache
def f(n):
    """
    持っている整数がnのときの確率
    f(n) = 1/6 x (f(n) + f(2n) + ... + f(6n))
    f(n) = 1/5 x (f(2n) + ... + f(6n))
    """
    if n == N:
        return 1
    if n > N:
        return 0
    rev = 0
    for i in range(2, M + 1):
        rev += f(i * n)
        rev %= MOD
    return rev * pow(5, -1, MOD) % MOD


print(f(1))
