import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
d = [[] for _ in range(N + 1)]

for i in range(N):
    a, b = map(int, input().split())
    d[a].append(i + 1)
    d[b].append(i + 1)

# DFS
from collections import deque

todo = deque([0])
seen = [False] * (N + 1)
seen[0] = True
while todo:
    v = todo.pop()
    for w in d[v]:
        if seen[w]:
            continue
        todo.append(w)
        seen[w] = True

print(sum(seen) - 1)
