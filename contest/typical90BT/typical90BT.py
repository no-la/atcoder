import sys

input = lambda: sys.stdin.readline().rstrip()
H, W = map(int, input().split())
C = [input() for _ in range(H)]
N = H * W

# 全探索
ans = -1

for s in range(N):
    todo = [(s, 1 << s)]
    while todo:
        v, route = todo.pop()
        vi, vj = divmod(v, W)
        if C[vi][vj] == "#":
            continue
        for di, dj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
            wi, wj = vi + di, vj + dj
            w = wi * W + wj
            if not (0 <= wi < H and 0 <= wj < W):
                continue
            if C[wi][wj] == "#":
                continue
            if w == s and route.bit_count() >= 3:
                ans = max(ans, route.bit_count())
                continue
            if route & (1 << w):
                continue
            todo.append((w, route | (1 << w)))

print(ans)
