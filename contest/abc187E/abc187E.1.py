class Tree:
    """木構造のあれこれをするクラス
    
    Attributes
    ----------
    parent[i]: 頂点iの親
    childs[i]: 頂点iの直接の子のリスト
    depth[i]: 頂点iの深さ
    hierarchy[k]: 深さkの頂点のリスト
    edges[i]: 頂点iから出る辺の行先のリスト
    leafs: 葉のリスト
    """
    
    def __init__(self, n, root) -> None:
        """
        Parameters
        ----------
        n : int
            頂点の個数
        root : int
            根
        """
        self.N = n
        self.root = root
        self.edges = [[] for _ in range(n)]
    
    def add_edge(self, from_, to, is_directed=True):
        self.edges[from_].append(to)
        if is_directed:
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
E = []
tree = Tree(N, 0)
for _ in range(N-1):
    a, b = map(lambda x: int(x)-1, input().split())
    tree.add_edge(a, b, True)
    E.append((a, b))
tree.set_info()

print("childs", tree.childs)
print("edges", tree.edges)

from functools import cache
#メモ化再帰
@cache
def f(tar, root):# rootを根とする部分木にtarが含まれているかどうか 含まれているならrootの次の根を返す
    for r in tree.childs[root]:
        if r==tar:
            return tar
        
        tree_with_tar = f(tar, r)
        if tree_with_tar is not None:
            return tree.parent[tree_with_tar]
    return None


Q = int(input())
imos = [0]*N
for _ in range(Q):
    t, e, x = map(int, input().split())
    e -= 1
    if t==1:
        a, b = E[e]
    else:
        a, b = E[e][::-1]
        
    # aを始点に、bを通らずに到達できる点に +xする
    par = f(a, b)
    if par is not None: # aがbを根とする部分木に含まれるとき
        imos[par] += x
    else:
        imos[b] -= x
        imos[tree.root] += x
    
    print("-"*10)
    print(a, "->", b, "+", x, imos)
    if par is not None:
        print("parent", par)

# DFS
from collections import deque
todo = deque([tree.root])
while todo:
    v = todo.pop()
    for w in tree.childs[v]:
        todo.append(w)
        imos[w] += imos[v]

print(*imos, sep="\n")
