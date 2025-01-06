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


if __name__ == "__main__":
    N = 5
    E = [[1], [0, 2, 3], [1, 4], [1], [2]]
    # 0 - 1 - 2 - 4
    #       - 3
    print(tree_based_dp(size=N, edges=E))  # 部分木の頂点番号の最大値
