N, M = map(int, input().split())
from collections import defaultdict
d = defaultdict(list)
for _ in range(M):
    a, b = map(lambda x: int(x)-1, input().split())
    d[a].append(b)
    d[b].append(a)


# BFSで各部屋から部屋1までの最短ルートを探す
# 部屋1から各部屋までの最短距離を探せばいい
#BFS
from collections import deque
todo = deque([0])
INF = 10**10
dist = [INF]*N #todo[0]からの距離のリスト
dist[todo[0]] = 0
while todo:
    v = todo.popleft()
    for w in d[v]:
        if dist[w]!=INF: #既に調べた点は飛ばす
            continue
        todo.append(w)
        dist[w] = dist[v]+1

ans = [-1]*N
for i in range(N):
    if ans[i]!=-1:
        print("No")
        exit()
    ans[i] = min([(dist[j], j) for j in d[i]])[1]+1
print("Yes")
print("\n".join(map(str, ans[1:])))