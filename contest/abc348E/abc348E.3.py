N = int(input())
E = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    E[a].append(b)
    E[b].append(a)

C = list(map(int, input().split()))

# 全方位木DP
from collections import deque


def tree_based_dp(size, edges, root=0):
    """木DP

    Parameters
    ----------
    size: 頂点数
    edges: 隣接リスト
    root: 根

    Example
    -------
    デフォルト引数は、dp[i]: 頂点iを根とする部分木の頂点番号の最大値を返す

    Usage
    -----
    eが初期値でない場合もあるため、適切に変更する
    """
    dp_c = [0] * size
    dp_d = [0] * size
    directed_edges = [[] for _ in range(size)]

    # DFS
    todo = deque([(root,)])
    seen = [False] * size
    seen[root] = True
    while todo:
        v, *others = todo.pop()
        if v == -1:
            v, w = others
            dp_c[v] += dp_c[w]
            dp_d[v] += dp_d[w] + dp_c[w]
            # dp_d[v]
            # = sum([C[x]*(d(v, x) + 1) for x in tree of v])
            # = sum([C[x]*d(v, x) for x in tree of w]) + sum([C[x] for x in tree of w]) (d(v, v)=0に注意)
            # = dp_d[w] + dp_c[w]
            continue
        dp_c[v] = C[v]
        for w in edges[v]:
            if seen[w]:
                continue
            todo.append((-1, v, w))
            todo.append((w,))
            seen[w] = True
            directed_edges[v].append(w)

    return dp_c, dp_d, directed_edges


def rerooting(size, edges, dp_c, dp_d, root=0):
    """

    Parameters
    ----------
    size: 頂点数
    edges: 隣接リスト
    dp: rootを根としたときの各部分木の値
    root: 根
    e: 単位元
    merge: 値をマージする関数

    """
    inverse_dp = [0] * size
    rerooted_dp = [0] * size

    # DFS
    todo = deque([(root, None, 0)])  # (頂点, 親, 何番目の子か)
    cumsum_right = [[] for _ in range(size)]
    cumsum_left = [[] for _ in range(size)]
    while todo:
        v, vp, vi = todo.pop()
        # vにおける各値を計算する
        if vp is not None:
            # 問題設定に応じて適切にマージする
            inverse_dp[v] = (
                inverse_dp[vp]
                + cumsum_left[vp][vi + 1]
                + cumsum_right[vp][vi]
                + (dp_c[0] - dp_c[v])
            )
            rerooted_dp[v] = inverse_dp[v] + dp_d[v]
        else:  # 根
            inverse_dp[v] = 0
            rerooted_dp[v] = dp_d[v]

        # 子の準備
        cumsum_left[v].append(0)
        cumsum_right[v].append(0)
        for wi, w in enumerate(edges[v]):
            todo.append((w, v, wi))
            cumsum_right[v].append(cumsum_right[v][-1] + dp_d[w] + dp_c[w])
        for wi, w in enumerate(reversed(edges[v])):
            cumsum_left[v].append(cumsum_left[v][-1] + dp_d[w] + dp_c[w])
        cumsum_left[v].reverse()
    # print(f"{inverse_dp=}")
    # print(f"{cumsum_left=}")
    # print(f"{cumsum_right=}")
    return rerooted_dp


dp_c, dp_d, directed_E = tree_based_dp(size=N, edges=E, root=0)
rerooted_dp = rerooting(size=N, edges=directed_E, dp_c=dp_c, dp_d=dp_d)
print(min(rerooted_dp))
# print(f"{rerooted_dp=}")
# print(f"{dp_c=}")
# print(f"{dp_d=}")
# print(f"{directed_E=}")
