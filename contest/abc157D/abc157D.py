N, M, K = map(int, input().split())
from collections import defaultdict
A = defaultdict(list)
C = defaultdict(set)
for _ in range(M):
    a, b = map(lambda x: int(x)-1, input().split())
    A[a].append(b)
    A[b].append(a)
for _ in range(K):
    c, d = map(lambda x: int(x)-1, input().split())
    C[c].add(d)
    C[d].add(c)


from collections import deque
seen = [None]*N
for i in range(N):
    #BFS
    if seen[i] is not None:
        continue
    todo = deque([i])
    p = set(todo)
    seen[todo[0]] = p
    while todo:
        v = todo.popleft()
        for w in A[v]:
            if seen[w] is not None: #既に調べた点は飛ばす
                continue
            if w in C[v]:
                continue
            todo.append(w)
            p.add(w)
            seen[w] = p

# 各点に対して、その点を含む友達マップから、既に友達である人数(既に友達 in 友達マップ)と、友達マップ内のブロックしてる人数を引く
print(" ".join([str(len(seen[i])-1-len(A[i])-len(C[i]&seen[i])) for i in range(N)]))