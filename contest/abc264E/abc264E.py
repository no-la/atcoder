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


N, M, E = map(int, input().split())
d = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(E)]
Q = int(input())
querry = list(int(input()) - 1 for _ in range(Q))
X = set(querry)
# クエリ逆読み
uf = UnionFind(N + M)
for i in range(E):
    if i not in X:
        uf.union(*d[i])

count = 0
seen = set()
for i in range(N, N + M):
    p = uf.find(i)
    if p in seen:
        count -= 1
        continue
    seen.add(p)
    count += uf.size[p] - 1

ans = []
for x in querry[::-1]:
    ans.append(count)
    u, v = sorted(d[x])
    up = uf.find(u)
    vp = uf.find(v)
    if up not in seen and vp >= N:
        count += uf.size[up]
    elif vp not in seen and up >= N:
        count += uf.size[vp]
    uf.union(u, v)


print(*ans[::-1], sep="\n")
