from collections import deque
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
d = {}
for i in range(M):
    if A[i] not in d:
        d[A[i]] = [B[i]]
    else:
        d[A[i]].append(B[i])
    if B[i] not in d:
        d[B[i]] = [A[i]]
    else:
        d[B[i]].append(A[i])

ans = [-1]*(N+1)
todo = deque(set(A)|set(B))
while todo:
    v = todo.pop()
    if ans[v]==-1:
        ans[v] = 0
    nx = 0 if ans[v]==1 else 1 
    for w in d[v]:
        if ans[w]==ans[v]:
            print("No")
            exit()
        elif ans[w]==-1:
            ans[w] = nx
            todo.append(w)
        else:
            pass

print("Yes")
        