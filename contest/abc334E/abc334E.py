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


def f(i, j):
    return i * W + j


def g(v):
    return divmod(v, W)


H, W = map(int, input().split())
S = [input() for _ in range(H)]
MOD = 998244353

uf = UnionFind(H * W)

for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            continue
        for di, dj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
            ni, nj = i + di, j + dj
            if not (0 <= ni < H and 0 <= nj < W):
                continue
            if S[ni][nj] == ".":
                continue
            uf.union(f(i, j), f(ni, nj))

# print(uf.parents)

green_sum = len(
    set([uf.find(f(i, j)) for i in range(H) for j in range(W) if S[i][j] == "#"])
)

bunshi = 0
bunbo = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            continue
        adjacents = set()
        for di, dj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
            ni, nj = i + di, j + dj
            if not (0 <= ni < H and 0 <= nj < W):
                continue
            if S[ni][nj] == ".":
                continue
            adjacents.add(uf.find(f(ni, nj)))

        bunbo += 1
        bunshi += green_sum - len(adjacents) + 1
        # print(i, j, adjacents)

ans = bunshi * pow(bunbo, -1, MOD) % MOD
print(ans)
# print(bunshi, "/", bunbo)
