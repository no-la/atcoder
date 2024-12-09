from collections import defaultdict


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

        self.da = [0] * n
        self.db = [0] * n

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

        self.da[y] += self.da[x]
        self.db[y] += self.db[x]


N, M, K = map(int, input().split())
E = []
for _ in range(M):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    E.append((w, u, v))
E.sort()

uf = UnionFind(N)

A = list(map(lambda x: int(x) - 1, input().split()))
B = list(map(lambda x: int(x) - 1, input().split()))
for a in A:
    uf.da[a] += 1
for b in B:
    uf.db[b] += 1


ans = 0
for w, u, v in E:
    if uf.find(u) == uf.find(v):
        continue

    uf.union(u, v)
    p = uf.find(u)
    delta = min(uf.da[p], uf.db[p])
    ans += w * delta
    uf.da[p] -= delta
    uf.db[p] -= delta


print(ans)
