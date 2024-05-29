H, W = map(int, input().split())
S = [input() for _ in range(H)]

# 白と接しているところだけ見ればいい
is_edge = [[None]*W for _ in range(H)]
corners = []
for i in range(H):
    for j in range(W):
        c = 0
        for di, dj in [[0, -1],[0, 1],[-1, 0],[1, 0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<H and 0<=nj<W:
                c +=  S[i+di][j+dj]=="."

        is_edge[i][j] = c
        if c>=2 and S[i][j]=="#":
            corners.append([i, j])

# print(corners)
# print(*is_edge, sep="\n")

from collections import deque
ans = 0
seen = [False]*len(corners)
for i in range(len(corners)):
    if seen[i]:
        continue
    # DFS
    todo = deque([i])
    ans += 4
    while todo:
        v = todo.pop()
        for w in range(len(corners)):
            if seen[w]: # 既に調べた点は飛ばす
                continue
            if corners[v][0]==corners[w][0] or corners[v][1]==corners[w][1]:
                todo.append(w)
                seen[w] = True

print(ans)
