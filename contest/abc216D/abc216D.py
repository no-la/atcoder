N, M = map(int, input().split())
d = []
di = [[] for _ in range(N+1)]
for i in range(M):
    k = int(input())
    d.append(list(map(int, input().split())))
    di[d[-1][0]].append(i)
# print(d)

# 同じ色は2個ずつしかないので、順番は関係ない
# DFS
from collections import deque
il = [0]*M
todo = deque([])
seen = [False]*(N+1) # ここはsetでもよい
for i in range(1, N+1):
    if seen[i]:
        continue
    if len(di[i])<2:
        continue
    
    todo.append(i)
    while todo:
        v = todo.pop()
        for j in di[v]:
            il[j] += 1
            if il[j]<len(d[j]):
                di[d[j][il[j]]].append(j)
                if len(di[d[j][il[j]]])==2:
                    todo.append(d[j][il[j]])
                    seen[d[j][il[j]]] = True
        # print(i, v, il)

print("Yes" if all([il[i]==len(d[i]) for i in range(M)]) else "No")
                