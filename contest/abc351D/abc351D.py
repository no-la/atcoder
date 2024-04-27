H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

# 動けないマスを$にする
for i in range(H):
    for j in range(W):
        if S[i][j]=="#":
            continue
        for di, dj in [[0, -1],[0, 1],[-1, 0],[1, 0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<H and 0<=nj<W and S[ni][nj]=="#":
                S[i][j] = "$"
                break
# print(*S, sep="\n")


ans = 1

from collections import deque
started = [[False]*W for _ in range(H)] # ここはsetでもよい
for i in range(H):
    for j in range(W):
        if started[i][j]:
            continue
        if S[i][j]!=".":
            continue
        # DFS
        started[i][j] = True
        todo = deque([(i, j)])
        seen = set()
        count = 1
        while todo:
            vi, vj = todo.pop()
            for di, dj in [[0, -1],[0, 1],[-1, 0],[1, 0]]:
                wi, wj = vi+di, vj+dj
                if not (0<=wi<H and 0<=wj<W):
                    continue
                if started[wi][wj]: # 既に調べた点は飛ばす
                    continue
                if S[wi][wj]=="#":
                    continue
                if (wi, wj) in seen:
                    continue
                
                count += 1
                if S[wi][wj]==".":
                    started[wi][wj] = True
                    todo.append((wi, wj))
                else:
                    seen.add((wi, wj))
        # print(i, j, count)

        ans = max(ans, count)

# print(*started, sep="\n")
print(ans)
