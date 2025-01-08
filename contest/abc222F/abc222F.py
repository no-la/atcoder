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

    directed_edges = [[] for _ in range(size)]

    # DFS
    todo = deque([(root,)])
    seen = [False] * size
    seen[root] = True
    while todo:
        v, *others = todo.pop()
        if v == -1:
            v, w, c = others
            dp[v] = merge(dp[v], dp[w] + c, c + D[w])
            continue

        for w, c in edges[v]:
            if seen[w]:
                continue
            todo.append((-1, v, w, c))
            todo.append((w,))
            seen[w] = True

            directed_edges[v].append((w, c))

    return dp, directed_edges


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
    todo = deque([(root, None, 0, 0)])  # (頂点, 親, 何番目の子か, そこへ向かう辺の重み)
    cumsum_right = [[] for _ in range(size)]
    cumsum_left = [[] for _ in range(size)]
    while todo:
        v, vp, vi, vc = todo.pop()
        # vにおける各値を計算する
        if vp is not None:
            # 問題設定に応じて適切にマージする
            inverse_dp[v] = merge(
                inverse_dp[vp] + vc,
                cumsum_right[vp][vi] + vc,
                cumsum_left[vp][vi + 1] + vc,
                vc + D[vp],
            )
            rerooted_dp[v] = merge(inverse_dp[v], dp[v])
        else:  # 根
            inverse_dp[v] = e
            rerooted_dp[v] = dp[v]

        # 子の準備
        cumsum_left[v].append(e)
        cumsum_right[v].append(e)
        for wi, (w, wc) in enumerate(edges[v]):
            todo.append((w, v, wi, wc))
            cumsum_right[v].append(merge(cumsum_right[v][-1], dp[w] + wc, wc + D[w]))
        for wi, (w, wc) in enumerate(reversed(edges[v])):
            cumsum_left[v].append(merge(cumsum_left[v][-1], dp[w] + wc, wc + D[w]))
        cumsum_left[v].reverse()
    # print(f"{inverse_dp=}")
    # print(f"{cumsum_right=}")
    # print(f"{cumsum_left=}")
    return rerooted_dp


N = int(input())
E = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    E[a].append((b, c))
    E[b].append((a, c))
D = list(map(int, input().split()))
dp, directed_edges = tree_based_dp(size=N, edges=E)
rerooted_dp = rerooting(size=N, edges=directed_edges, dp=dp)
print(*rerooted_dp, sep="\n")
# print(f"{dp=}", f"{directed_edges=}", sep="\n")
