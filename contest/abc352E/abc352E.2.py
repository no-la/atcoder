class UnionFind():
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root, y_root = self.find(x), self.find(y)
        if x_root == y_root:
            return False
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1
        return True

N, M = map(int, input().split())
edges = []
for _ in range(M):
    w, *vertices = map(int, input().split())
    edges.append((w, vertices))

edges.sort()
uf = UnionFind(N)
total_weight = 0
for weight, vertices in edges:
    if uf.union(*vertices):
        total_weight += weight
print(total_weight if uf.find(0) == uf.find(N - 1) else -1)
