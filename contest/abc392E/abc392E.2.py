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


import sys

input = lambda: sys.stdin.readline().rstrip()
N, M = map(int, input().split())

uf = UnionFind(N)

# 連結成分ごとに1辺ずつ外に出す気持ち
# ただし一つだけそのままにしていい
# 連結成分内で辺が余っていない場合、他の連結成分から貰う
d = [[] for _ in range(N)]
# d[i]: 親をiとする連結成分で余っている辺のindexのlist

E = []
delay_E = []
for i in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    E.append((a, b))

    if a == b:
        delay_E.append((i, a, b))
        continue

    ap, bp = uf.find(a), uf.find(b)
    if ap == bp:
        d[ap].append(i)
    else:
        uf.union(a, b)

for i, a, b in delay_E:
    d[uf.find(a)].append(i)

from collections import deque

todo = deque([i for i in range(N) if uf.find(i) == i])

if len(todo) == 1:
    print(0)
    exit()

ans = []

while todo:
    p = todo.popleft()
    if not d[p]:
        todo.append(p)
    while todo and d[p]:
        np = todo.popleft()
        if p == np:
            todo.append(np)
            continue
        edge = d[p].pop()
        # edgeをnpに繋ぎかえる
        # print(p, "->", np)
        ans.append(tuple(map(lambda x: x + 1, [edge, E[edge][0], np])))

# print(ROOTS)
print(len(ans))
for l in ans:
    print(*l)
