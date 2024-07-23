N, M = map(int, input().split())
S = [input() for _ in range(N)]

# 調べる必要のある移動は岩の個数x12程度なので、全探索でよい
ans = [[False]*M for _ in range(N)]
ans[1][1] = True

# DFS
from collections import deque
todo = deque([(1, 1)])
seen = [[False]*M for _ in range(N)] # ここはsetでもよい
seen[1][1] = True
while todo:
    vi, vj = todo.pop()
    for di, dj in [[0, -1],[0, 1],[-1, 0],[1, 0]]:
        wi, wj = vi+di, vj+dj
        while 0<=wi<N and 0<=wj<M and S[wi][wj]==".":
            ans[wi][wj] = True
            wi += di
            wj += dj
        wi -= di
        wj -= dj
        if seen[wi][wj]:
            continue
        todo.append((wi, wj))
        seen[wi][wj] = True
        
# print(*ans, sep="\n")
print(sum(list(map(sum, ans))))
