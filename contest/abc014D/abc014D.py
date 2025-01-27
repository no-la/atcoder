import sys

sys.setrecursionlimit(100000)


class SegTree:
    def __init__(self, num, e, operator=max):
        """
        parameter
            num : 要素数
            e : 単位元(初期値)
            operator : 2つの子ノードの値から親ノードの値を作る関数
        """
        # self.tree[i+self.offset]:要素iのみの区間の値
        self.offset = 1 << (num - 1).bit_length()
        self.tree = [e] * (self.offset << 1)
        self.e = e
        self.operator = operator

    def update(self, i, value):
        """i番目の要素をvalueにする"""
        i += self.offset
        self.tree[i] = value
        # 親ノードを順に変更していく
        while i > 1:
            v1, v2 = self.tree[i], self.tree[i ^ 1]  # 子ノード
            i >>= 1  # iを親ノードへずらす
            self.tree[i] = self.operator(v1, v2)

    def get_point(self, p):
        """p番目の要素を取得する"""
        return self.tree[p + self.offset]

    def get_range(self, l, r):
        """区間[l, r)の値を取得する"""
        l += self.offset
        r += self.offset

        ans = self.e
        while l < r:
            if r & 1:
                ans = self.operator(ans, self.tree[r - 1])
                r -= 1
            if l & 1:
                ans = self.operator(ans, self.tree[l])
                l += 1
            l >>= 1
            r >>= 1
        return ans


N = int(input())
from collections import defaultdict

E = defaultdict(list)
for _ in range(N - 1):
    x, y = map(lambda x: int(x) - 1, input().split())
    E[x].append(y)
    E[y].append(x)

euler_tour = []
first_appear = [None] * N

ROOT = 0
seen = [False] * N


def dfs(d, v):
    if first_appear[v] is None:
        first_appear[v] = len(euler_tour)
    euler_tour.append((d, v))

    for w in E[v]:
        if seen[w]:
            continue
        seen[w] = True
        dfs(d + 1, w)
        euler_tour.append((d, v))


seen[ROOT] = True
dfs(0, ROOT)

INF = 10**15
st = SegTree(len(euler_tour), (INF, 0), min)
for i in range(len(euler_tour)):
    st.update(i, euler_tour[i])

Q = int(input())
for _ in range(Q):
    a, b = map(lambda x: int(x) - 1, input().split())
    ai, bi = first_appear[a], first_appear[b]
    if ai > bi:
        ai, bi = bi, ai
    lca = st.get_range(ai, bi + 1)
    ans = euler_tour[ai][0] + euler_tour[bi][0] - 2 * lca[0] + 1
    # print(a, b, lca)
    print(ans)

# print(euler_tour, first_appear, sep="\n")
