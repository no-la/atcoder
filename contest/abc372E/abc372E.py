class UnionFind:
    """
    集合を木と捉え、各要素にその根を持たせる
    Union : 2つの木を合併する
    Find : 要素の根を返す
    """

    def __init__(self, n) -> None:
        """
        parameter
            n : 要素数
        """
        self.n = n
        self.parents = [-1] * n
        self.rank = [0] * n
        self.size = [1] * n
        self.top = [[i] for i in range(n)]

    def find(self, x):
        """
        xの根を返す
        """
        if self.parents[x] == -1:
            return x
        else:
            # 値を更新しながら根を探す
            # 深さは最大でlog(n)なので、再帰関数でok
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        """
        xを含む木とyを含む木を合併する
        """
        x = self.find(x)
        y = self.find(y)
        nsize = self.size[x] + self.size[y]

        if x == y:
            return

        if self.rank[x] > self.rank[y]:
            x, y = y, x

        self.parents[x] = y

        if self.rank[x] == self.rank[y]:
            self.rank[y] += 1

        self.size[x] = nsize
        self.size[y] = nsize

        self.top[y] = sorted(self.top[y] + self.top[x], reverse=True)[:10]


N, Q = map(int, input().split())

uf = UnionFind(N)

for _ in range(Q):
    t, *x = map(int, input().split())
    if t == 1:
        u, v = x
        u -= 1
        v -= 1
        uf.union(u, v)
    else:
        v, k = x
        v -= 1
        k -= 1
        vp = uf.find(v)
        print(uf.top[vp][k] + 1 if k < uf.size[vp] else -1)
