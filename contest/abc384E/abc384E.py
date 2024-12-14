H, W, X = map(int, input().split())
P, Q = map(lambda x: int(x) - 1, input().split())
S = [list(map(int, input().split())) for _ in range(H)]

from heapq import heapify, heappop, heappush

strength = 0
todo = []
heapify(todo)
heappush(todo, (S[P][Q], P, Q))
seen = [[False] * W for _ in range(H)]
seen[P][Q] = True
while todo:
    # (vi, vj) を吸収できるかぎりする
    _, vi, vj = heappop(todo)
    if strength > 0 and X * S[vi][vj] >= strength:
        break
    strength += S[vi][vj]
    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        wi, wj = vi + di, vj + dj
        if not (0 <= wi < H and 0 <= wj < W):
            continue
        if seen[wi][wj]:
            continue
        heappush(todo, (S[wi][wj], wi, wj))
        seen[wi][wj] = True

print(strength)
