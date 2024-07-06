N = int(input())
S = input()+".."
T = input()+".."

if S==T:
    print(0)
    exit()
# Nちっさ。気付かなかった
# BFS
from collections import deque
from collections import defaultdict
todo = deque([S])
dist = defaultdict(int)
dist[S] = 0
while todo:
    # print(todo)
    v = todo.popleft()
    tar = v.index(".")
    for i in range(N+1):
        if not (i+1<tar or tar+1<i):
            continue
        l = list(v)
        l[i:i+2], l[tar:tar+2] = l[tar:tar+2], l[i:i+2]
        # print(l)
        w = "".join(l)
        if w==T:
            print(dist[v]+1)
            exit()
        if dist[w]!=0: # 既に調べた点は飛ばす
            continue
        todo.append(w)
        dist[w] = dist[v]+1
        # print(dist[w], w)

print(-1)
