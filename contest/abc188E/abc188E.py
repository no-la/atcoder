N, M = map(int, input().split())
A = list(map(int, input().split()))
from collections import defaultdict
d = defaultdict(list)
for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    d[x].append(y)


from collections import deque
ans = 0
seen = [False]*N # ここはsetでもよい
for i in range(N):
    if seen[i]:
        continue
    seen[i] = True
    min_, max_ = A[i], A[i]
    # DFS
    todo = deque([i])
    while todo:
        v = todo.pop()
        for w in d[v]:
            if seen[w]: # 既に調べた点は飛ばす
                continue
            todo.append(w)
            seen[w] = True
            min_ = min(A[w], min_)
            max_ = max(A[w], max_)
    ans = max(ans, max_-min_)

print(ans)            
