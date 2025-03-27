"""NS"""

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
MOD = 10**9 + 7
N = int(input())
C = input().split()
edges = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    edges[a - 1].append(b - 1)
    edges[b - 1].append(a - 1)

from collections import deque


def tree_based_dp(size, edges, root=0, e=0, merge=max):
    """木DP

    Parameters
    ----------
    size: 頂点数
    edges: 隣接リスト
    root: 根
    e: 単位元
    merge: 値をマージする関数
    value_of_leaf: 葉における値を返す関数

    Example
    -------
    デフォルト引数は、dp[i]: 頂点iを根とする部分木の頂点番号の最大値を返す

    Usage
    -----
    eが初期値でない場合もあるため、適切に変更する
    """
    dp = [[e] * 3 for _ in range(size)]
    # dp[i][x]: 頂点iを根とする部分木を考えたときの場合の数 ただしiの連結成分は、x=0: aだけ, x=1: bだけ, x=2: aもbもある

    # DFS
    todo = deque([(root,)])
    seen = [False] * size
    seen[root] = True
    children = [[] for _ in range(size)]
    while todo:
        v, *others = todo.pop()
        if v == -1:
            v, w = others

            children[v].append(w)
            if len(children[v]) < len(edges[v]) - (v != root):
                continue

            # vのすべての子wに対してdp[w]が定まっている
            i = C[v] != "a"
            j = i ^ 1
            dp[v][i] = 1
            dp[v][j] = 0
            dp[v][2] = 1
            temp = 1
            for w in children[v]:
                dp[v][i] *= dp[w][i] + dp[w][2]
                dp[v][i] %= MOD

                dp[v][2] *= dp[w][0] + dp[w][1] + 2 * dp[w][2]
                dp[v][2] %= MOD

                temp *= dp[w][i] + dp[w][2]
                temp %= MOD

            dp[v][2] -= temp
            dp[v][2] %= MOD
            continue

        for w in edges[v]:
            if seen[w]:
                continue
            todo.append((-1, v, w))
            todo.append((w,))
            seen[w] = True

        if len(edges[v]) <= 1:  # 葉
            if C[v] == "a":
                dp[v][0] = 1
            else:
                dp[v][1] = 1
    return dp


dp = tree_based_dp(N, edges)
print(dp[0][2])
