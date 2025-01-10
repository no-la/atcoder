from collections import defaultdict, deque


def topological_sort(N, edges):
    indeg = [0] * N
    for v in range(N):
        for w in edges[v]:
            indeg[w] += 1

    todo = deque([v for v in range(N) if indeg[v] == 0])
    S = []
    while todo:
        v = todo.popleft()
        S.append(v)
        for w in edges[v]:
            indeg[w] -= 1
            if indeg[w] == 0:
                todo.append(w)

    return S


N = int(input())
ids = defaultdict(lambda: None)
strs = []
E = [[] for _ in range(2 * N)]
for _ in range(N):
    s, t = input().split()
    si, ti = ids[s], ids[t]
    if si is None:
        si = len(strs)
        ids[s] = si
        strs.append(s)
    if ti is None:
        ti = len(strs)
        ids[t] = ti
        strs.append(t)

    E[si].append(ti)

M = len(strs)

sorted_list = topological_sort(M, E)
print("Yes" if len(sorted_list) == M else "No")
