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
        self.updated = [False]*n
        self.max_size = 1
    
    def find(self, x):
        """
        xの根を返す
        """
        if self.parents[x]==-1:
            self.updated[x] = True
            return x
        else:
            if self.updated[x]:
                return self.parents[x]
            
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
        self.max_size = max(self.max_size, nsize)
        
        self.updated[x] = False
        self.updated[y] = False

N, M = map(int, input().split())
uf = UnionFind(N)
E = [] # E[_]: 辺の重み, 繋げる頂点の集合
for _ in range(M):
    E.append([list(map(int, input().split()))[1]])
    E[-1].append(list(map(lambda x: int(x)-1, input().split())))

# print(*E, sep="\n")


E.sort()
ans = 0
# print(uf.parents)
for i in range(M):
    C, A = E[i]
    k = 0
    for j in range(1, len(A)):
        if uf.find(A[j])==uf.find(A[k]):
            continue
        # print(A[j], A[k])
        uf.union(A[j], A[k])
        ans += C
    if uf.max_size==N:
        break
else:
    # print(uf.parents)
    print(-1)
    exit()

print(ans)
