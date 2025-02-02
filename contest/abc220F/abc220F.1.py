from collections import deque


class RerootingDP:
    def __init__(
        self,
        size,
        edges,
        root=0,
        e=0,
        merge=max,
        put_edge=lambda val, v, w, c: val,
        put_vertex=lambda val, vertex: val,
    ):
        """
        Parameters
        ----------
        size: 頂点数
        edges: 隣接リスト
        root: 根
        e: 単位元
        merge: 値をマージする関数
        put_edge(val, v, w, c): valをなすwの部分木に辺v-w(重みc)を追加したときの演算
        put_vertex(val, vertex): valをなすwの部分木に頂点vertexを追加したときの演算
        """
        self.size = size
        self.edges = edges
        self.root = root
        self.e = e
        self.merge = merge
        self.put_edge = put_edge
        self.put_vertex = put_vertex

        self.dp = [self.e] * self.size
        self.rerooted_dp = [self.e] * self.size

        self.directed_edges = [[] for _ in range(self.size)]

        self.size_at = [1] * self.size
        # 各部分木のサイズ

    def do(self):
        self.tree_based_dp()
        self.rerooting()
        return self.rerooted_dp

    def tree_based_dp(self):
        todo = deque([(self.root,)])
        seen = [False] * self.size
        seen[self.root] = True
        while todo:
            v, *others = todo.pop()
            if v == -1:  # 戻るときに値を更新する
                v, w, c = others
                self.dp[v] = self.merge(
                    self.dp[v], self.put_edge(self.dp[w], v, w, self.size_at[w])
                )
                self.size_at[v] += self.size_at[w]
                continue

            for w, c in self.edges[v]:
                if seen[w]:
                    continue
                todo.append((-1, v, w, c))
                todo.append((w,))
                seen[w] = True

                # 次いでに作っておく
                self.directed_edges[v].append((w, c))

    def rerooting(self):
        inverse_dp = [self.e] * self.size
        todo = deque(
            [(self.root, None, 0, 0)]
        )  # (頂点, 親, 何番目の子か, そこへ向かう辺の重み)
        cumsum_right = [[] for _ in range(self.size)]
        cumsum_left = [[] for _ in range(self.size)]
        while todo:
            v, vp, vi, vc = todo.pop()
            # vにおける各値を計算する
            if vp is not None:
                # 問題設定に応じて適切にマージする
                inverse_dp[v] = (
                    self.merge(
                        self.put_edge(inverse_dp[vp], v, vp, 0),
                        self.merge(
                            self.put_edge(cumsum_right[vp][vi], v, vp, 0),
                            self.put_edge(cumsum_left[vp][vi + 1], v, vp, 0),
                        ),
                    )
                    + self.size  # 妥協的な実装
                    - self.size_at[v]
                )
                self.rerooted_dp[v] = self.put_vertex(
                    self.merge(inverse_dp[v], self.dp[v]), v
                )
            else:  # 根
                inverse_dp[v] = self.e
                self.rerooted_dp[v] = self.dp[v]

            # 子の準備
            cumsum_left[v].append(self.e)
            cumsum_right[v].append(self.e)
            for wi, (w, wc) in enumerate(self.directed_edges[v]):
                todo.append((w, v, wi, wc))
                cumsum_right[v].append(
                    self.merge(
                        cumsum_right[v][-1],
                        self.put_edge(self.dp[w], v, w, self.size_at[w]),
                    )
                )
            for wi, (w, wc) in enumerate(reversed(self.directed_edges[v])):
                cumsum_left[v].append(
                    self.merge(
                        cumsum_left[v][-1],
                        self.put_edge(self.dp[w], v, w, self.size_at[w]),
                    )
                )
            cumsum_left[v].reverse()


def put_edge(val, v, w, c):
    return val + c


def put_vertex(val, v):
    return val


N = int(input())
E = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = map(lambda x: int(x) - 1, input().split())
    E[u].append((v, 1))
    E[v].append((u, 1))

rdp = RerootingDP(
    size=N,
    edges=E,
    root=0,
    e=0,
    merge=lambda x, y: x + y,
    put_edge=put_edge,
    put_vertex=put_vertex,
)
print(*rdp.do(), sep="\n")
