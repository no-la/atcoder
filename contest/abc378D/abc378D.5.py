H, W, K = map(int, input().split())
S = [input() for _ in range(H)]

ans = 0


def f(seen, i, j):
    global ans
    if len(seen) == K + 1:
        ans += 1
        return
    if len(seen) > K + 1:  # 念のため
        return

    for di, dj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
        ni, nj = i + di, j + dj
        if not (0 <= ni < H and 0 <= nj < W):
            continue
        if S[ni][nj] == "#":
            continue
        if (ni, nj) in seen:
            continue

        seen.add((ni, nj))
        f(seen, ni, nj)
        seen.remove((ni, nj))


for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            f(set([(i, j)]), i, j)

print(ans)
