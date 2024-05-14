N = int(input())
A = tuple(map(lambda x: int(x)-1, input().split()))
B = tuple(map(lambda x: int(x)-1, input().split()))
S = [input() for _ in range(N)]



# BFS
from collections import deque
todo = deque([A])
dist = [[None]*N for _ in range(N)]
dist[A[0]][A[1]] = 0
while todo:
    vi, vj = todo.popleft()
    ndist = dist[vi][vj] + 1
    for sgn in [[1, 1],[-1, 1],[1, -1],[-1, -1]]:
        for d in range(1, N):
            wi, wj = vi+sgn[0]*d, vj+sgn[1]*d
            if not (0<=wi<N and 0<=wj<N):
                break
            if S[wi][wj]=="#":
                break
            if dist[wi][wj]!=None and dist[wi][wj]<ndist: # 既に調べた点は飛ばす
                break
            todo.append((wi, wj))
            dist[wi][wj] = ndist

ans = dist[B[0]][B[1]] 
if ans is None:
    ans = -1
# print(*dist, sep="\n")
print(ans)
