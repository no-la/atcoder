a, N = map(int, input().split())

ans = float("inf")

# 逆向きの操作でN->1を調べる

#BFS
from collections import deque
todo = deque([N])
dist = [-1]*(N*10)
dist[N] = 0
while todo:
    v = todo.popleft()
    l = []
    temp = str(v)
    if v>=10 and temp[1]!="0":
        l.append(int(temp[1:]+temp[0]))
    if v%a==0:
        l.append(v//a)
    for w in l:
        if dist[w]!=-1: #既に調べた点は飛ばす
            continue
        nd = dist[v]+1
        if w==1:
            ans = min(nd, ans)
        todo.append(w)
        dist[w] = nd

print(ans if ans!=float("inf") else -1)