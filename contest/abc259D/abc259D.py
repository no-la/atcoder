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

N = int(input())
sx, sy, tx, ty = map(int, input().split())

uf = UnionFind(N)
C = []
S = []
T = []
for i in range(N):
    x, y, r = map(int, input().split())
    C.append((x, y, r))
    if (x-sx)**2+(y-sy)**2==r**2:
        S.append(i)
    if (x-tx)**2+(y-ty)**2==r**2:
        T.append(i) 
    
if not S or not T:
    print("No")
    exit()

def f(x1, y1, r1, x2, y2, r2): # 交点があるかの判定
    d = (x1-x2)**2+(y1-y2)**2
    if d > (r1+r2)**2:
        return False
    if (r1-r2)**2 <= d <= (r1+r2)**2:
        return True
    else:
        return False

for i in range(N):
    ix, iy, ir = C[i]
    for j in range(N):
        jx, jy, jr = C[j]
        
        # if (ix-jx)**2+(iy-jy)**2<=(ir+jr)**2:
        if f(ix, iy, ir, jx, jy, jr):
            uf.union(i, j)

for si in S:
    for ti in T:
        if uf.find(si)==uf.find(ti):
            print("Yes")
            exit()

print("No")
