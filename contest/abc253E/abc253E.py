N, M, K = map(int, input().split())
MOD = 998244353

from functools import cache
#メモ化再帰
@cache
def f(x, n):
    # 長さnで最後がxの数列の残りを埋めるときの答え
    l , r = x-K, x+K
    if n==N-1:
        # print(x, n)
        return (max(0, l)+max(0, M-r+1))%MOD
    rev = 0
    for y in range(1, l+1):
        rev += f(y, n+1)
        rev %= MOD
    for y in range(r, M+1):
        rev += f(y, n+1)
        rev %= MOD
    # print(x, n, rev)
    return rev

ans = 0
for x in range(1, M+1):
    ans += f(x, 1)
    ans %= MOD
print(ans)