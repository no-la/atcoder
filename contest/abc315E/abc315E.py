N = int(input())
edges = []
# edges[_] = (a, b) : aを読んでからbを読む
d = [[] for _ in range(N)]
# d[i]: iを読むために読む必要のある本のlist

for i in range(N):
    c, *temp = map(int, input().split())
    for j in temp:
        j -= 1
        edges.append((j, i))
        d[i].append(j)

from collections import deque

target_vertexes = set()
# DFS
from collections import deque

todo = deque([0])
seen = [False] * N
seen[0] = True
while todo:
    v = todo.pop()
    for w in d[v]:
        if seen[w]:
            continue
        todo.append(w)
        seen[w] = True
        target_vertexes.add(w)


def topological_sort(N, edges):
    indeg = [0] * N
    to = [[] for _ in range(N)]
    for a, b in edges:
        indeg[b] += 1
        to[a].append(b)

    todo = deque([v for v in range(N) if indeg[v] == 0][::-1])
    S = []
    while todo:
        v = todo.popleft()
        for w in to[v]:
            indeg[w] -= 1
            if indeg[w] == 0:
                todo.append(w)
        S.append(v)

    return S


print(
    *map(
        lambda x: x + 1,
        [v for v in topological_sort(N, edges=edges) if v in target_vertexes],
    )
)
