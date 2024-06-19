N, X = map(int, input().split())

from functools import cache
#メモ化再帰
@cache
def f(n, x):
    # レベルnのバーガーの下からx層を食べるときのパティの個数
    if n==0:
        return 1
    ans = 0
    
    x -= 1 # パン
    if x>0: # レベルn-1バーガー
        if x>g(n-1):
            ans += f(n-1, g(n-1))
        else:
            ans += f(n-1, x)
        x -= g(n-1)
    if x>0: # パティ
        ans += 1
        x -= 1
    if x>0: # レベルn-1バーガー
        if x>g(n-1):
            ans += f(n-1, g(n-1))
        else:
            ans += f(n-1, x)
        x -= g(n-1)
    x -= 1
    
    return ans

def g(n):
    # レベルnのバーガーの層の数
    return 2**(n+2)-3


print(f(N, X))
