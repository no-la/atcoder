N, X, Y = map(int, input().split())
X -= 1
Y -= 1
d = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = map(lambda x: int(x) - 1, input().split())
    d[u].append(v)
    d[v].append(u)

# DFS
from collections import deque

todo = deque([X])
seen = [False] * N  # ここはsetでもよい
seen[todo[0]] = True
before = [None] * N
while todo:
    v = todo.pop()
    for w in d[v]:
        if seen[w]:  # 既に調べた点は飛ばす
            continue
        todo.append(w)
        seen[w] = True
        before[w] = v

ans = [Y + 1]
p = Y
while before[p] is not None:
    ans.append(before[p] + 1)
    p = before[p]

print(*ans[::-1])
