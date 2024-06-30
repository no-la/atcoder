N, K = map(int, input().split())
MOD = 998244353

Ninv2 = pow(N, -2, MOD)
P = (2*N-2)*Ninv2%MOD # 黒が動く確率
Q = (N**2-2*N+2)*Ninv2%MOD # 動かない確率

import sys

sys.setrecursionlimit(1000000)
from functools import cache
#メモ化再帰
@cache
def f(x, count): # xからK-count回操作した後の位置の期待値
    if count==K:
        return x
    rev = Q*f(x, count+1)
    for i in range(1, N+1):
        if i==x:
            continue
        rev += (2*Ninv2)*f(i, count+1)
        rev %= MOD
    return rev

print(f(1, 0))
