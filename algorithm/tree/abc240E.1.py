# https://atcoder.jp/contests/abc240/submissions/52744568
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
        for to, from_ in self.E:
            self.edges[from_].append(to)

        if not self.is_directed:
            for to, from_ in self.E:
                self.edges[to].append(from_)
    
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

N = int(input())
t = Tree(N, [list(map(lambda x: int(x)-1, input().split())) for _ in range(N-1)],
         0, False)

ans = [[1, 0] for _ in range(N)]

# 葉の値を、条件を満たすようにおく
for c, i in enumerate(t.leafs):
    ans[i] = [c+1, c+1]
    
# 順に親へ向かっていき、区間が最小になるように値を決めていく
for h in t.hierarchy[::-1]:
    for i in h:
        if not t.childs[i]:
            continue
        ans[i][1] = max([ans[c][1] for c in t.childs[i]])
        ans[i][0] = min([ans[c][0] for c in t.childs[i]])
        
for l, r in ans:
    print(l, r)
    