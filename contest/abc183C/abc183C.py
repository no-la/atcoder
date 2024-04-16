N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]

ans = 0

# O(8!)=40320
# DFS
from collections import deque
todo = deque([(0, 0)])
dist = [None]*N # ここはsetでもよい
while todo:
    *v, cost = todo.pop()
    if isinstance(v, int):
        v = list(v)
    if len(v)==N:
        ans += (cost+T[v[-1]][0])==K
        continue
    for w in range(N):
        if w in v:
            continue
        todo.append(v.copy()+[w]+[cost+T[v[-1]][w]])
print(ans)