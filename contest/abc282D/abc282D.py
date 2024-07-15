class UnionFind():
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
        self.parents = [-1]*n
        self.rank = [0]*n
        self.size = [1]*n
    
    def find(self, x):
        """
        xの根を返す
        """
        if self.parents[x]==-1:
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
        nsize = self.size[x]+self.size[y]
    
        if x==y:
            return
        
        if self.rank[x] > self.rank[y]:
            x, y = y, x
        
        self.parents[x] = y
        
        if self.rank[x] == self.rank[y]:
            self.rank[y] += 1
        
        self.size[x] = nsize
        self.size[y] = nsize
        
N, M = map(int, input().split())
from collections import defaultdict
d = defaultdict(list)
uf = UnionFind(N)
for _ in range(M):
    u, v = map(lambda x: int(x)-1, input().split())
    d[u].append(v)
    d[v].append(u)
    uf.union(u, v)

from collections import deque
b = [None]*N
for i in range(N):
    if b[i] is not None:
        continue
    b[i] = 0
    # BFS
    todo = deque([i])
    while todo:
        v = todo.popleft()
        for w in d[v]:
            if b[w] is not None: # 既に調べた点は飛ばす
                if b[w]!=b[v]^1:
                    print(0)
                    exit()
                continue
            todo.append(w)
            b[w] = b[v]^1

# print(b)
# print(uf.parents)

ans1 = 0
ans2 = 0
for i in range(N):
    if uf.parents[i]!=-1:
        continue
    
    
    ans1 += uf.size[i]*(N-uf.size[i])
    
    c = b[i]
    ec = 0
    todo = [i]
    seen = set([i])
    while todo:
        v = todo.pop()
        for w in d[v]:
            ec += 1
            if w in seen:
                continue
            seen.add(w)
            c += b[w]
            todo.append(w)
    
    ec //= 2
    ans2 += c*(uf.size[i]-c) - ec
    # print(i, uf.size[i], c, ec)

print(ans1//2 + ans2)
    