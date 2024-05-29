H, W = map(int, input().split())
S = [input() for _ in range(H)]

# 白と接しているところだけ見ればいい
d = [[None]*W for _ in range(H)]
start = None
for i in range(H):
    for j in range(W):
        if S[i][j]==".":
            d[i][j] = 0
            continue
        c = 0
        for di, dj in [[0, -1],[0, 1],[-1, 0],[1, 0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<H and 0<=nj<W:
                c +=  S[i+di][j+dj]=="."

        d[i][j] = c
        if c>=2 and S[i][j]=="#":
            start = [i, j]

print(start)
print(*d, sep="\n")

ans = d[start[0]][start[1]]
# DFS
from collections import deque
todo = deque([start])
seen = [[False]*W for _ in range(H)] # ここはsetでもよい
seen[start[0]][start[1]] = True
while todo:
    vi, vj = todo.pop()
    for di, dj in [[0, -1],[0, 1],[-1, 0],[1, 0]]:
        wi, wj = vi+di, vj+dj
        if not (0<=wi<H and 0<=wj<W):
            continue
        if seen[wi][wj]: # 既に調べた点は飛ばす
            continue
        if d[wi][wj]>=1:
            todo.append([wi, wj])
            seen[wi][wj] = True
            ans += (d[wi][wj]-1)

print(ans)
