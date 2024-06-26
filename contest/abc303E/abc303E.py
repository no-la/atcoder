N = int(input())
from collections import defaultdict
d = defaultdict(list)
deg = [0]*N
for _ in range(N-1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    d[u].append(v)
    d[v].append(u)
    deg[u] += 1
    deg[v] += 1
    

# 次数1の点から始める
for i in range(N):
    if deg[i]==1:
        s = i
        break

ans = []
# DFS
from collections import deque
todo = deque([(s, 0)])
seen = [False]*N # ここはsetでもよい
seen[s] = True
while todo:
    v, vc = todo.pop()
    wc = (vc+1)%3
    for w in d[v]:
        if seen[w]: # 既に調べた点は飛ばす
            continue
        if deg[w]>1: # 次数1の点は調べる必要なし
            if wc==1: # もともと星の中心だった点
                ans.append(deg[w])
            todo.append((w, wc))
            seen[w] = True

print(*sorted(ans))
