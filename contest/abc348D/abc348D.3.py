H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]
for i in range(H):
    for j in range(W):
        if A[i][j]=="S":
            start = (i, j)
        
N = int(input())
D = []
for i in range(N):
    r, c, e = map(int, input().split())
    if A[r-1][c-1]!="T":
        A[r-1][c-1] = e
        D.append((r-1, c-1))

# O(NHW)
if not isinstance(A[start[0]][start[1]], int):
    print("No")
    exit()

from collections import deque, defaultdict
d = defaultdict(set) # 行き来できる薬の座標の有向グラフ
for r, c in D:
    # BFS
    todo = deque([(r, c)])
    dist = [[-1]*W for _ in range(H)] #todo[0]からの距離のリスト
    dist[r][c] = 0
    while todo:
        vi, vj = todo.popleft()
        if dist[vi][vj]>=A[r][c]:
            continue
        for di, dj in [(0, -1),(0, 1),(-1, 0),(1, 0)]:
            wi, wj = vi+di, vj+dj
            if not (0<=wi<H and 0<=wj<W):
                continue
            if A[wi][wj]=="#":
                continue
            if dist[wi][wj]!=-1: # 既に調べた点は飛ばす
                continue
            if isinstance(A[wi][wj], int) or A[wi][wj]=="T":
                d[(r, c)].add((wi, wj))
            todo.append((wi, wj))
            dist[wi][wj] = dist[vi][vj]+1

# print(*A, sep="\n")
# print(*d.items(), sep="\n")

# DFS
todo = deque([start])
seen = set(todo[0]) # ここはsetでもよい
while todo:
    v = todo.pop()
    for w in d[v]:
        if w in seen: # 既に調べた点は飛ばす
            continue
        if A[w[0]][w[1]]=="T":
            print("Yes")
            exit()
        todo.append(w)
        seen.add(w)
print("No")