N = int(input())
from collections import defaultdict
d = defaultdict(list)
for _ in range(N-1):
    u, v = map(lambda x: int(x)-1, input().split())
    d[u].append(v)
    d[v].append(u)


depth = []
parent = list(range(N))
leafs = []
# BFS
from collections import deque
todo = deque([0])
dist = [-1]*N #todo[0]からの距離のリスト
dist[todo[0]] = 0
depth.append([[0]])
while todo:
    v = todo.popleft()
    ndist = dist[v]+1
    if ndist==len(depth):
        depth.append([])
    depth[ndist].append([])
    if len(d[v])==1 and v!=0:
        leafs.append(v)
    for w in d[v]:
        if dist[w]!=-1: # 既に調べた点は飛ばす
            continue
        todo.append(w)
        dist[w] = ndist
        parent[w] = v
        depth[ndist][-1].append(w)


# print("parent", parent)
# print("depth", *depth, sep="\n")
# print("leafs", leafs)

leaf_num = [0]*N # 自身も含む
for leaf in leafs:
    i = leaf
    while parent[i]!=i:
        leaf_num[i] += 1
        i = parent[i]
    leaf_num[0] += 1

# print("leaf_num", leaf_num)

ans = [[1, 1] for _ in range(N)]
for ll in depth: # 階層
    for l in ll:
        if not l:
            continue
        ans[l[0]][0] = ans[parent[l[0]]][0]
        ans[l[0]][1] = ans[l[0]][0] + leaf_num[l[0]]-1
        for i in range(len(l)-1):
            ans[l[i+1]][0] = ans[l[i]][1]+1
            ans[l[i+1]][1] = ans[l[i+1]][0] + leaf_num[l[i+1]]-1

print(*[f"{l} {r}" for l, r in ans], sep="\n")