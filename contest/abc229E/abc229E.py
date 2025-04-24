import sys

input = lambda: sys.stdin.readline().rstrip()


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


N, M = map(int, input().split())
E = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    E[a].append(b)

uf = UnionFind(N)
ans = [0]

for a in range(N - 1, -1, -1):
    temp = ans[-1] + 1
    for b in E[a]:
        if uf.find(a) != uf.find(b):
            uf.union(a, b)
            temp -= 1
    ans.append(temp)
print(*ans[:-1][::-1], sep="\n")
