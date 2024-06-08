N = int(input())
A = list(map(lambda x: int(x)-1, input().split()))

indeg = [0]*N
for i in range(N):
    indeg[A[i]] += 1

ans = 0

size = [None]*N

# 閉路
from collections import deque
seen = [False]*N
for s in range(N):
    if seen[s] or indeg[s]==0:
        continue
    # DFS
    points = [s]
    todo = deque([s])
    seen[s] = True
    while todo:
        v = todo.pop()
        if seen[A[v]]:
            break
        seen[A[v]] = True
        todo.append(A[v])
        points.append(A[v])
    flag = False
    cpoints = []
    for p in points:
        if not flag:
            flag = p == A[v]
        if not flag:
            continue
        cpoints.append(p)
    count = len(cpoints)
    ans += count*count
    for p in cpoints:
        size[p] = count
# print(ans)
# print(size)

starts = [i for i in range(N) if indeg[i]==0]
seen = [False]*N
for s in starts:
    count = 1
    tocount = 0
    v = s
    seen[v] = True
    fin = False
    while size[v] is None:
        v = A[v]
        if seen[v]:
            fin = True
        if not fin:
            seen[v] = True
            count += 1
        else:
            tocount += 1
    count -= 1
    if tocount:
        count += 1
        tocount -= 1
    # print(s, count, tocount, A[v], size[A[v]])
    ans += count + (count-1)*count//2
    ans += count*tocount
    ans += count*size[v]

print(ans)
