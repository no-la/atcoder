from collections import deque


def tree_diameter(N: int, d: list):
    """木の直径を求める

    Parameters
    ----------
    N : 木のサイズ
    d[i] : i から行ける頂点 j について (j, i-jのコスト) のlist
    """
    # 1回目
    todo_from_0 = deque([0])
    dist_from_0 = [-1] * N
    dist_from_0[todo_from_0[0]] = 0
    while todo_from_0:
        v = todo_from_0.popleft()
        for w, c in d[v]:
            if dist_from_0[w] != -1:  # 既に調べた点は飛ばす
                continue
            todo_from_0.append(w)
            dist_from_0[w] = dist_from_0[v] + c

    u = max([(v, i) for i, v in enumerate(dist_from_0)])[1]

    # 2回目
    todo_from_u = deque([u])
    dist_from_u = [-1] * N
    dist_from_u[todo_from_u[0]] = 0
    while todo_from_u:
        v = todo_from_u.popleft()
        for w, c in d[v]:
            if dist_from_u[w] != -1:  # 既に調べた点は飛ばす
                continue
            todo_from_u.append(w)
            dist_from_u[w] = dist_from_u[v] + c

    diameter = max(dist_from_u)
    return diameter


N = int(input())
d = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    d[a].append((b, 1))
    d[b].append((a, 1))

# 木の直径 + 1
# が答え

print(tree_diameter(N, d) + 1)
