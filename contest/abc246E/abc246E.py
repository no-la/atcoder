N = int(input())
A = tuple(map(lambda x: int(x)-1, input().split()))
B = tuple(map(lambda x: int(x)-1, input().split()))
S = [input() for _ in range(N)]


def f(wi, wj):
    if not (0<=wi<N and 0<=wj<N):
        return False
    if dist[wi][wj]!=None: # 既に調べた点は飛ばす
        return False
    if S[wi][wj]=="#":
        return False
    return True

# BFS
from collections import deque
todo = deque([A])
dist = [[None]*N for _ in range(N)]
dist[A[0]][A[1]] = 0
while todo:
    vi, vj = todo.popleft()
    for d in range(1, N):
        wi, wj = vi-d, vj-d
        if f(wi, wj):
            todo.append((wi, wj))
            dist[wi][wj] = dist[vi][vj]+1
        else:
            break
    
    for d in range(1, N):
        wi, wj = vi+d, vj-d
        if f(wi, wj):
            todo.append((wi, wj))
            dist[wi][wj] = dist[vi][vj]+1
        else:
            break
    for d in range(1, N):
        wi, wj = vi-d, vj+d
        if f(wi, wj):
            todo.append((wi, wj))
            dist[wi][wj] = dist[vi][vj]+1
        else:
            break
    for d in range(1, N):
        wi, wj = vi+d, vj+d
        if f(wi, wj):
            todo.append((wi, wj))
            dist[wi][wj] = dist[vi][vj]+1
        else:
            break

ans = dist[B[0]][B[1]] 
if ans is None:
    ans = -1
# print(*dist, sep="\n")
print(ans)
