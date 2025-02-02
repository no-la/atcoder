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
                # NOTE: put_edge, put_vertexの導入
                # self.dp[v] = self.merge(self.dp[v], self.dp[w] + c, c + D[w])
                self.dp[v] = self.merge(self.dp[v], self.put_edge(self.dp[w], v, w, c))
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

                # NOTE: put_edge, put_vertexの導入
                # inverse_dp[v] = self.merge(
                #     inverse_dp[vp] + vc,
                #     cumsum_right[vp][vi] + vc,
                #     cumsum_left[vp][vi + 1] + vc,
                #     vc + D[vp],
                # )
                inverse_dp[v] = self.merge(
                    self.put_edge(inverse_dp[vp], v, vp, vc),
                    self.merge(
                        self.put_edge(cumsum_right[vp][vi], v, vp, vc),
                        self.put_edge(cumsum_left[vp][vi + 1], v, vp, vc),
                    ),
                )
                # NOTE: put_edge, put_vertexの導入
                # self.merge(inverse_dp[v], self.dp[v]), v
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
                # NOTE: put_edge, put_vertexの導入
                # cumsum_right[v].append(
                #     self.merge(cumsum_right[v][-1], self.dp[w] + wc, wc + D[w])
                # )
                cumsum_right[v].append(
                    self.merge(cumsum_right[v][-1], self.put_edge(self.dp[w], v, w, wc))
                )
            for wi, (w, wc) in enumerate(reversed(self.directed_edges[v])):
                # NOTE: put_edge, put_vertexの導入
                # cumsum_left[v].append(
                #     self.merge(cumsum_left[v][-1], self.dp[w] + wc, wc + D[w])
                # )
                cumsum_left[v].append(
                    self.merge(cumsum_left[v][-1], self.put_edge(self.dp[w], v, w, wc))
                )
            cumsum_left[v].reverse()


def put_edge(val, v, w, c):
    return max(val + c, c + D[w])


def put_vertex(val, v):
    return val


N = int(input())
E = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    E[a].append((b, c))
    E[b].append((a, c))
D = list(map(int, input().split()))


rdp = RerootingDP(
    size=N, edges=E, root=0, e=0, merge=max, put_edge=put_edge, put_vertex=put_vertex
)
print(*rdp.do(), sep="\n")
# print(f"{dp=}", f"{directed_edges=}", sep="\n")
