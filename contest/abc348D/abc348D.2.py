H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]
for i in range(H):
    for j in range(W):
        if A[i][j]=="S":
            start = (i, j)
        elif A[i][j]=="T":
            goal = (i, j)
        
N = int(input())
for i in range(N):
    r, c, e = map(int, input().split())
    if A[r-1][c-1]!="T":
        A[r-1][c-1] = e

# O(NHW)
if not isinstance(A[start[0]][start[1]], int):
    print("No")
    exit()

# BFS
from collections import deque
todo = deque([(*start, A[start[0]][start[1]])])
energy = [[-1]*W for _ in range(H)]
energy[start[0]][start[1]] = A[start[0]][start[1]]
while todo:
    vi, vj, ve = todo.popleft()
    if ve==0:
        continue
    for di, dj in [(0, -1),(0, 1),(-1, 0),(1, 0)]:
        wi, wj, we = vi+di, vj+dj, ve-1
        if not (0<=wi<H and 0<=wj<W):
            continue
        if A[wi][wj]=="#":
            continue
        if isinstance(A[wi][wj], int):
            we = max(we, A[wi][wj])
        if energy[wi][wj]<we:
            todo.append((wi, wj, we))
            energy[wi][wj] = we

print("Yes" if energy[goal[0]][goal[1]]!=-1 else "No")