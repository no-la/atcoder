from collections import deque


def tree_based_dp(size, edges, root=0):
    """木DP

    Parameters
    ----------
    size: 頂点数
    edges: 隣接リスト
    root: 根
    e: 単位元
    merge: 値をマージする関数

    Example
    -------
    デフォルト引数は、dp[i]: 頂点iを根とする部分木の頂点番号の最大値を返す

    Usage
    -----
    eが初期値でない場合もあるため、適切に変更する
    """
    dp = [0] * size
    dp_size = [0] * size

    directed_edges = [[] for _ in range(N)]

    # DFS
    todo = deque([(root,)])
    seen = [False] * size
    seen[root] = True
    while todo:
        v, *others = todo.pop()
        if v == -1:
            v, w = others
            dp_size[v] += dp_size[w]
            dp[v] += dp[w] + dp_size[w]
            # dp[v]
            # = sum([dis(v, j) for j in children_of(v)])
            # = sum([sum([dis(w, j) + 1 for j in children_of(w)]) for w in children_of(w)])
            # = sum([dp[w] + dp_size[w] for w in children_of(w)])
            continue
        dp_size[v] = 1
        for w in edges[v]:
            if seen[w]:
                continue
            todo.append((-1, v, w))
            todo.append((w,))
            seen[w] = True

            directed_edges[v].append(w)

    return dp, dp_size, directed_edges


def rerooting(size, edges, dp, dp_size, root=0):
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
    rerooted_dp = [0] * size
    inverse_dp = [0] * size

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
                + cumsum_right[vp][vi]
                + cumsum_left[vp][vi + 1]
                + (dp_size[root] - dp_size[v])
            )
            rerooted_dp[v] = inverse_dp[v] + dp[v]
        else:  # 根
            inverse_dp[v] = 0
            rerooted_dp[v] = dp[v]

        # 子の準備
        cumsum_left[v].append(0)
        cumsum_right[v].append(0)
        for wi, w in enumerate(edges[v]):
            todo.append((w, v, wi))
            cumsum_right[v].append(cumsum_right[v][-1] + dp[w] + dp_size[w])
        for wi, w in enumerate(reversed(edges[v])):
            cumsum_left[v].append(cumsum_left[v][-1] + dp[w] + dp_size[w])
        cumsum_left[v].reverse()
    # print(f"{inverse_dp=}")
    # print(f"{cumsum_left=}")
    # print(f"{cumsum_right=}")
    return rerooted_dp


N = int(input())
E = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = map(lambda x: int(x) - 1, input().split())
    E[u].append(v)
    E[v].append(u)

dp, dp_size, directed_edges = tree_based_dp(size=N, edges=E)
rerooted_dp = rerooting(size=N, edges=directed_edges, dp=dp, dp_size=dp_size)
print(*rerooted_dp, sep="\n")
# print(f"{dp=}")
# print(f"{dp_size=}")
# print(f"{directed_edges=}")
