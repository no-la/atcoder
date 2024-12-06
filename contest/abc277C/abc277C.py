N = int(input())
from collections import defaultdict

d = defaultdict(list)
for _ in range(N):
    a, b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)

# DFS
from collections import deque

ans = 1
todo = deque([1])
seen = set([1])
while todo:
    v = todo.pop()
    for w in d[v]:
        if w in seen:
            continue
        todo.append(w)
        seen.add(w)
        ans = max(ans, w)

print(ans)
