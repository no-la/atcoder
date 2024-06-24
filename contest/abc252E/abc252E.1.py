N, M = map(int, input().split())
from collections import defaultdict
A = defaultdict(list)
for i in range(M):
    a, b, c = map(int, input().split())
    A[a-1].append((b-1, c, i))
    A[b-1].append((a-1, c, i))

d = [10**15]*N # d[i]: 0->iのコスト
e = [None]*N # e[i]: 現在採用しているiに向かう辺のid

# DFS
from collections import deque
todo = deque(A[0])
seen = [False]*M # ここはsetでもよい
for b, c, i in A[0]:
    d[b] = c
    e[b] = i
    seen[i] = True
while todo:
    v, vc, vi = todo.popleft()
    for w, wc, wi in A[v]:
        if seen[wi]: # 既に調べた点は飛ばす
            continue
        seen[wi] = True
        # print(d, e, f"{v} to {w}", sep="\n")
        # print(d[v], wc, d[w])
        if d[v]+wc<d[w] and d[v]<d[w]:
            d[w] = d[v]+wc
            e[w] = wi
            todo.append((w, wc, wi))
        elif d[w]+wc<d[v]:
            d[v] = d[w]+wc
            e[v] = wi
            todo.append((w, wc, wi))
ans = []
for i in range(1, N):
    ans.append(e[i]+1)

print(*ans)
