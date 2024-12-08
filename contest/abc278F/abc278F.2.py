N = int(input())
S = [input() for _ in range(N)]

d = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if S[i][-1] == S[j][0]:
            d[i].append(j)

from functools import cache


@cache
def f(i, b):
    """
    勝利するプレイヤーを変えす
    i: 現在の頂点
    b: 通った頂点のbit
    """
    turn = b.bit_count() % 2
    for j in d[i]:
        if b & (1 << j):
            continue
        res = f(j, b | (1 << j))
        if res == turn:
            return turn
    return turn ^ 1


for i in range(N):
    if f(i, 1 << i) == 0:
        print("First")
        exit()
print("Second")
