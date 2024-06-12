H, W = map(int, input().split())
C = [input() for _ in range(H)]

for i in range(H):
    for j in range(W):
        if C[i][j]=="S":
            si, sj = i, j
            break

tar = []
for di, dj in [[0, -1],[0, 1],[-1, 0],[1, 0]]:
    i, j = si+di, sj+dj
    if not (0<=i<H and 0<=j<W):
        continue
    if C[i][j]==".":
        tar.append((i, j))

from collections import deque
for s in tar:
    # DFS
    todo = deque([s])
    seen = [[False]*W for _ in range(H)] # ここはsetでもよい
    seen[s[0]][s[1]] = True
    while todo:
        vi, vj = todo.pop()
        for di, dj in [[0, -1],[0, 1],[-1, 0],[1, 0]]:
            wi, wj = vi+di, vj+dj
            if not (0<=wi<H and 0<=wj<W):
                continue
            if seen[wi][wj]: # 既に調べた点は飛ばす
                continue
            if C[wi][wj]==".":
                todo.append((wi, wj))
                seen[wi][wj]= True
                if (wi, wj) in tar:
                    print("Yes")
                    exit()

print("No")
