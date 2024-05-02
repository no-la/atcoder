class Tree:
    """木構造のあれこれをするクラス
    
    Attributes
    ----------
    N: 超点数
    E[i]: (i番目の辺の始点, 終点)
    parent[i]: 頂点iの親
    childs[i]: 頂点iの直接の子のリスト
    depth[i]: 頂点iの深さ
    hierarchy[k]: 深さkの頂点のリスト
    edges[i]: 頂点iから出る辺の行先のリスト
    leafs: 葉のリスト
    """
    
    def __init__(self, n, e, root, is_directed=True) -> None:
        """
        Parameters
        ----------
        n : int
            頂点の個数
        root : int
            根
        e: list of int
            各辺の(始点, 終点)のlist
        """
        self.N = n
        self.E = e
        self.root = root
        self.edges = [[] for _ in range(n)]
        self.is_directed = is_directed
        
        self.set_edges()
        self.set_info()
    
    def set_edges(self):
        for from_, to in self.E:
            self.edges[from_].append(to)

        if not self.is_directed:
            for to, from_ in self.E:
                self.edges[from_].append(to)
    
    def set_info(self):
        """深さごとの頂点のリスト、親のリスト、子のリストを作る"""
        self.parent = [None]*self.N
        self.childs = [[] for _ in range(self.N)]
        self.hierarchy = []
        self.depth = [-1]*self.N
        self.leafs = []
        
        todo = [self.root]
        
        # 初期化
        self.depth[todo[0]] = 0
        self.parent[0] = self.root
        self.hierarchy.append([self.root])
        while todo:
            v = todo.pop()
            wdepth = self.depth[v]+1
            if wdepth>=len(self.hierarchy):
                self.hierarchy.append([])
            for w in self.edges[v]:
                if self.depth[w]!=-1:
                    continue                
                self.depth[w] = wdepth
                self.parent[w] = v
                self.hierarchy[wdepth].append(w)
                self.childs[v].append(w)
                
                todo.append(w)
            
            if not self.childs[v]:
                self.leafs.append(v)
            if not self.hierarchy[-1]:
                self.hierarchy.pop()
    
