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

    Example
    -------
    デフォルト引数は、dp[i]: 頂点iを根とする部分木の頂点番号の最大値を返す

    Usage
    -----
    eが初期値でない場合もあるため、適切に変更する
    """
    dp = [e] * size

    # DFS
    todo = deque([(root,)])
    seen = [False] * size
    seen[root] = True
    while todo:
        v, *others = todo.pop()
        if v == -1:
            v, w = others
            dp[v] = merge(dp[v], dp[w])
            continue

        for w in edges[v]:
            if seen[w]:
                continue
            todo.append((-1, v, w))
            todo.append((w,))
            seen[w] = True

        if len(edges[v]) <= 1:  # 葉
            dp[v] = v
    return dp


def rerooting(size, edges, dp, root=0, e=0, merge=max):
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
    rerooted_dp = [e] * size
    inverse_dp = [e] * size

    # DFS
    todo = deque([(root, None, 0)])  # (頂点, 親, 何番目の子か)
    cumsum_right = [[] for _ in range(size)]
    cumsum_left = [[] for _ in range(size)]
    while todo:
        v, vp, vi = todo.pop()
        # vにおける各値を計算する
        if vp:
            # 問題設定に応じて適切にマージする
            inverse_dp[v] = merge(inverse_dp[vp], v)
            rerooted_dp[v] = merge(
                inverse_dp[vp],
                merge(dp[v], merge(cumsum_right[vp][vi], cumsum_left[vp][vi])),
            )
        else:  # 根
            inverse_dp[v] = v
            rerooted_dp[v] = dp[v]

        # 子の準備
        cumsum_left[v].append(e)
        cumsum_right[v].append(e)
        for wi, w in enumerate(edges[v]):
            todo.append((w, v, wi))
            cumsum_right[v].append(merge(cumsum_right[v][-1], dp[w]))
        for wi, w in enumerate(reversed(edges[v])):
            cumsum_left[v].append(merge(cumsum_left[v][-1], dp[w]))
        cumsum_left[v].reverse()
    return rerooted_dp


if __name__ == "__main__":
    N = 5
    E = [[1], [2, 3], [4], [], []]
    # 0 - 1 - 2 - 4
    #       - 3
    dp = tree_based_dp(size=N, edges=E)
    print(dp)  # 部分木の頂点番号の最大値
    print(rerooting(size=N, edges=E, dp=dp))
