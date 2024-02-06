N, M = map(int, input().split())
from collections import defaultdict
d = defaultdict(list)
for _ in range(M):
    a, b = map(lambda x: int(x)-1, input().split())
    d[a].append(b)
    d[b].append(a)

#BFS
from collections import deque
seen = [-2]*N
for i in range(N): #各グループごとにDFSをして、1直線のグラフになっているか調べる
    if seen[i]!=-2:
        continue
    todo = deque([i])
    seen[todo[0]] = 0
    while todo:
        v = todo.popleft()
        if len(d[v])>2:
            print("No")
            exit()
        for w in d[v]:
            if seen[w]==seen[v]-1: #戻らない
                continue
            if seen[w]!=-2: #既に調べた点 円になってる
                print("No")
                exit()
            todo.append(w)
            seen[w] = seen[v]+1
print("Yes")