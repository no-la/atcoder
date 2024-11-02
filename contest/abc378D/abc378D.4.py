from collections import deque

H, W, K = map(int, input().split())
S = [input() for _ in range(H)]


ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            continue
        todo = deque([(i, j, set([(i, j)]))])
        while todo:
            vi, vj, vs = todo.pop()
            for di, dj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                wi, wj = vi + di, vj + dj
                if not (0 <= wi < H and 0 <= wj < W):
                    continue
                if S[wi][wj] == "#":
                    continue
                if (wi, wj) in vs:
                    continue
                if len(vs) == K:
                    ans += 1
                else:
                    todo.append((wi, wj, vs | set([(wi, wj)])))

print(ans)
