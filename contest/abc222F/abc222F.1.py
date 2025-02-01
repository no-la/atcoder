# https://atcoder.jp/contests/abc222/submissions/59322275
class RerootingDP:
    def __init__(self, N, E, merge, e, put_edge, put_vertex):
        """
        Parameters
        ----------
        N : 頂点数
        E : 辺のlist
        merge : dpの値の演算
        e : 単位元
        put_edge : 部分木への辺の追加（まだ頂点は追加しない）に付随する値の変更をする関数
        put_vertex : 部分木への頂点の追加に付随する値の変更をする関数
        """
        self.N = N
        self.E = E
        self.merge = merge
        self.e = e
        self.put_edge = put_edge
        self.put_vertex = put_vertex

        # to[v]: vから出ている辺のindex
        self.to = [[] for _ in range(self.N)]
        for i in range(len(self.E)):
            v, u = self.E[i]
            self.to[v].append(i)

    def reroot(self):
        E, to = self.E, self.to
        res = [None] * self.N
        dp = [self.e()] * self.N

        # まずは木DP
        stack = [(0, -1, 1, -1), (0, -1, 0, -1)]
        while stack:
            v, par, f, idx = stack.pop()
            if not f:  # 親から子へ進む
                for idx in to[v]:
                    _, u = E[idx]
                    if u == par:
                        continue
                    stack.append((u, v, 1, idx))
                    stack.append((u, v, 0, idx))
            else:  # 子から親へ戻る
                dp[v] = self.put_vertex(dp[v], v)
                if par != -1:
                    dp[par] = self.merge(dp[par], self.put_edge(dp[v], idx))

        # Rerootする
        acc_l = [[self.e()] * (len(to[v]) + 1) for v in range(self.N)]
        acc_r = [[self.e()] * (len(to[v]) + 1) for v in range(self.N)]
        dp_out = [-1] * self.N
        stack = [(0, -1, 0)]
        while stack:
            v, par, t = stack.pop()
            deg = len(to[v])
            if t == 0:
                for i in range(deg):
                    idx = to[v][i]
                    _, u = E[idx]
                    # 部分木uに辺v-uを追加した値を、acc_l[v][i]にmergeして、次の兄弟を含む累積和を作る
                    acc_l[v][i + 1] = self.merge(acc_l[v][i], self.put_edge(dp[u], idx))
                for i in range(deg - 1, -1, -1):
                    idx = to[v][i]
                    _, u = E[idx]
                    acc_r[v][i] = self.merge(acc_r[v][i + 1], self.put_edge(dp[u], idx))

                res[v] = dp[v] = self.put_vertex(acc_r[v][0], v)

                _, u = E[to[v][t]]
                if u == par:
                    dp_out[v] = self.put_vertex(
                        self.merge(acc_l[v][t], acc_r[v][t + 1]), v
                    )
                    stack.append((v, par, t + 1))
                    continue
                dp[v] = self.put_vertex(self.merge(acc_l[v][t], acc_r[v][t + 1]), v)

                stack.append((v, par, t + 1))
                stack.append((u, v, 0))
            elif t < deg:
                dp[v] = res[v]

                _, u = E[to[v][t]]
                if u == par:
                    dp_out[v] = self.put_vertex(
                        self.merge(acc_l[v][t], acc_r[v][t + 1]), v
                    )
                    stack.append((v, par, t + 1))
                    continue
                dp[v] = self.put_vertex(self.merge(acc_l[v][t], acc_r[v][t + 1]), v)

                stack.append((v, par, t + 1))
                stack.append((u, v, 0))
            else:
                dp[v] = dp_out[v]

        return res


import sys

input = sys.stdin.readline
N = int(input())
E = []
W = []
for i in range(N - 1):
    u, v, w = map(int, input().split())
    u, v = u - 1, v - 1
    E.append((u, v))
    W.append(w)
    E.append((v, u))
    W.append(w)
D = list(map(int, input().split()))


def put_edge(s, idx):
    v, u = E[idx]
    return max(s, D[u]) + W[idx]


def put_vertex(s, v):
    return s


rerooting = RerootingDP(N, E, max, lambda: -1 << 32, put_edge, put_vertex)
res = rerooting.reroot()
print(*res, sep="\n")
