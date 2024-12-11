N, K = map(int, input().split())
A = list(map(int, input().split()))

from functools import cache
import sys

sys.setrecursionlimit(10**8)


# メモ化再帰
@cache
def f(remain, turn):
    """remainだけ残っているときの勝者"""
    if remain == 0:
        return turn ^ 1
    for a in A:
        if remain - a >= 0:
            if f(remain - a, turn ^ 1) == turn:
                return turn
    return turn ^ 1


print(["First", "Second"][f(K, 0)])
