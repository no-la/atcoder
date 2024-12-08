N = int(input())
S = [input() for _ in range(N)]

# 有向グラフで考える
d = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if S[i][-1] == S[j][0]:
            d[i].append(j)


# 任意の始点からの経路を考えて、全て奇数長のものが存在すれば先手が勝てる
from functools import cache


@cache
def f(i, b):
    """
    bのビットが立っている頂点を通らずに、iから最後まで移動する経路の頂点数は、奇数のみ(1)、偶数のみ(0)、どちらもある(-1)
    """
    temp = set()
    for j in d[i]:
        if b & (1 << j):
            continue
        res = f(j, b | (1 << j))
        if res == -1:
            return -1
        temp.add(res)

    if not temp:
        return 1
    elif len(temp) == 2:
        return -1
    elif 0 in temp:
        return 1
    else:
        return 0


for i in range(N):
    if f(i, 1 << i) == 1:
        print("First")
        exit()

print("Second")
