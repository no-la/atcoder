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
    
        if x==y:
            return
        
        if self.rank[x] > self.rank[y]:
            x, y = y, x
        
        self.parents[x] = y
        
        if self.rank[x] == self.rank[y]:
            self.rank[y] += 1
    
    