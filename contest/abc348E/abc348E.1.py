N = int(input())
E = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    E[a].append(b)
    E[b].append(a)

C = list(map(int, input().split()))

# 全方位木DP
sum_c = [0]*N
sum_d = [0]*N
# sum_c[i]: 頂点iの部分木のの頂点xについてC[x]の総和
# sum_d[i]: 頂点iの部分木のの頂点xについてC[x]*d(i, x)の総和

# DFS
from collections import deque
todo = deque([0])
seen = [False]*N # ここはsetでもよい
seen[todo[0]] = True
while todo:
    v = todo.pop()
    for w in E[v]:
        if seen[w]: # 既に調べた点は飛ばす
            continue
        todo.append(w)
        ...
        