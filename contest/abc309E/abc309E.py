N, M = map(int, input().split())
P = [0] + list(map(lambda x: int(x)-1, input().split()))

d = [None for _ in range(N)] # d[i]: P[i]の深さ
d[0] = -1

import sys
sys.setrecursionlimit(1000000)
from functools import cache
#メモ化再帰
@cache
def f(n):
    parent = P[n]
    d[n] = (f(parent) if d[parent]==None else d[parent]) + 1
    return d[n]

for i in range(N):
    f(i)

# print(*d, sep="\n")

# imos法
imos = [[0]*(300010)]
#始点に+x, 終点の次の点に-xする

# 適当な処理
for i in range(1, len(imos)):
    imos[i] += imos[i-1]    
    
    

