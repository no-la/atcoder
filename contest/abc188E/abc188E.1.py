N, M = map(int, input().split())
A = list(map(int, input().split()))
from collections import defaultdict
d = defaultdict(list)
S = [True]*N
for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    d[x].append(y)
    S[y] = False


from collections import deque
ans = -10**10
seen = [False]*N # ここはsetでもよい
for i in range(N):
    if not S[i]:
        continue
    seen[i] = True
    # DFS
    todo = deque([(i, A[i])])
    while todo:
        v, vbought = todo.pop()
        for w in d[v]:
            # print(i, "to", w, A[w]-vbought)
            ans = max(ans, A[w]-vbought)
            wbought = min(vbought, A[w])
            todo.append((w, wbought))

print(ans)
