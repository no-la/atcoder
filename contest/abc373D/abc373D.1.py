from collections import deque

N, M = map(int, input().split())
d = [[] for _ in range(N)]
for _ in range(M):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    d[u].append((v, w))
    d[v].append((u, -w))
K = 10**18

ans = [None] * N

for i in range(N):
    if ans[i] is not None:
        continue
    ans[i] = 0
    # DFS
    todo = deque([i])
    while todo:
        v = todo.pop()
        for w, wc in d[v]:
            if ans[w] is not None:  # 既に調べた点は飛ばす
                continue
            todo.append(w)
            ans[w] = ans[v] + wc

print(*ans, sep=" ")
