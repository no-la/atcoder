from functools import cache
import sys

sys.setrecursionlimit(10**7)


N = int(input())


# メモ化再帰
@cache
def f(n):
    if n == 0:
        return 1
    return f(n // 2) + f(n // 3)


print(f(N))
