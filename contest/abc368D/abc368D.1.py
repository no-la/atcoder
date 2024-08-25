N, K = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(lambda x: int(x)-1, input().split())
    E[a].append(b)
    E[b].append(a)

V = list(map(lambda x: int(x)-1, input().split())) 

root = V[0]
parent = [None]*N

# DFS
from collections import deque
todo = deque([root])
seen = [False]*N # ここはsetでもよい
seen[todo[0]] = True
while todo:
    v = todo.pop()
    for w in E[v]:
        if seen[w]: # 既に調べた点は飛ばす
            continue
        todo.append(w)
        seen[w] = True
        parent[w] = v

# print(parent)

can_remove = [True]*N
for v in V:
    can_remove[v] = False
todo = V.copy()
while todo:
    v = todo.pop()
    w = parent[v]
    if w is None:
        continue
    if can_remove[w]:
       can_remove[w] = False
       todo.append(w)
 
print(can_remove.count(False))    
    