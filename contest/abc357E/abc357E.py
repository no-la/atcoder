N = int(input())
A = list(map(lambda x: int(x)-1, input().split()))

indeg = [0]*N
for i in range(N):
    indeg[A[i]] += 1

starts = [a for a in range(N) if indeg[a]==0]
fin = set()
ans = 0
from collections import deque
for s in starts:
    # DFS
    todo = deque([s])
    seen = set([s])
    count = 1
    while todo:
        v = todo.pop()
        if A[v] in seen:
            fin.add(A[v])
            break
        seen.add(A[v])
        todo.append(A[v])
        count += 1
    ans += (count)*(count-1)//2 + count

print(starts)
print(ans)

# 閉路ごと
seen = [False]*N
for s in range(N):
    if s in fin or indeg[s]==0:
        seen[s] = True
        continue
    if seen[s]:
        continue
    # DFS
    flag = False
    todo = deque([s])
    seen[s] = True
    count = 1
    while todo:
        v = todo.pop()
        if A[v] in fin:
            flag = True
            break
        if seen[A[v]]:
            break
        seen[A[v]] = True
        todo.append(A[v])
        count += 1
    if flag:
        continue
    ans += count + count*(count-1)//2
        
print(ans)
