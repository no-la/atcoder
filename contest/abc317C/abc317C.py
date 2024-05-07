N, M = map(int, input().split())
from collections import defaultdict
d = defaultdict(list)
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    d[a].append((b, c))
    d[b].append((a, c))


from collections import deque
ans = 0
for i in range(N):
    # DFS
    todo = deque([(i, 0)])
    seen = [False]*N # ここはsetでもよい
    seen[todo[0][0]] = True
    while todo:
        v, vc = todo.pop()
        for w, dc in d[v]:
            if seen[w]: # 既に調べた点は飛ばす
                ans = max(ans, vc+dc)
                continue
            todo.append((w, vc+dc))
            seen[w] = True

print(ans)
