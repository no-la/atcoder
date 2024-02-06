N, M = map(int, input().split())
from collections import defaultdict
d = defaultdict(list)
for _ in range(M):
    a, b = map(lambda x:int(x)-1, input().split())
    d[a].append(b) #a->b


g = []

#BFS
from collections import deque
dist = [None]*N #todo[0]からの距離のリスト
for i in range(N):
    if i not in d:
        continue
    if dist[i] is not None:
        continue
    todo = deque([i])
    dist[todo[0]] = 0
    temp = [i]
    while todo:
        v = todo.popleft()
        for w in d[v]:
            if dist[w]==dist[v]-1:
                continue
            if dist[w] is not None: #既に調べた点は飛ばす
                print(2)
                exit()
            todo.append(w)
            temp.append(w)
            dist[w] = dist[v]+1
    g.append("".join(sorted(map(lambda s:str(s+1), temp))))
g.sort(reverse=True) #降順
ans = []
for i in range(N):
    if dist[i] is None:
        ans.append(str(i+1))
    else:
        ans.append(g.pop())
print("".join(ans))