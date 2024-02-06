M = int(input())
from collections import defaultdict
d = defaultdict(list)
for _ in range(M):
    u, v = map(lambda x:int(x)-1, input().split())
    d[u].append(v)
    d[v].append(u)
P = list(map(lambda x:int(x)-1, input().split()))
for i in range(9):
    if i not in P:
        P.append(i)

#空の点を、コマ9が置かれていると考える
#9!=362660~4*10^5
#BFS
from collections import deque
todo = deque([P])
dist = defaultdict(lambda:-1) #todo[0]からの距離のリスト
dist[str(todo[0])] = 0
while todo:
    v = todo.popleft()
    i = str(v)
    for w in d[v[-1]]:
        nv = v.copy()
        temp = nv[-1]
        nv[-1] = w
        nv[nv.index(w)] = temp
        ni = str(nv)
        if dist[ni]!=-1: #既に調べた点は飛ばす
            continue
        todo.append(nv)
        dist[ni] = dist[i]+1
print(dist[str([i for i in range(9)])])