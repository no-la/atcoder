N = 3
H, W = 4, 4
P = [[input() for _ in range(H)] for _ in range(N)]


# 全探索？
# 回転で4通り、位置が4^2通り
# ミノが3個なので、全部で (4^3)^3 = 64^3 = 262144 ~ 2 x 10^6 通り


def rotate(mino):
    """90度回転"""
    rev = [[None] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            rev[i][j] = mino[W - 1 - j][i]
    return rev


def put(pre_grid, mino, offset_x, offset_y):
    grid = [[pre_grid[i][j] for j in range(W)] for i in range(H)]
    for dx in range(H):
        for dy in range(W):
            if mino[dx][dy] == ".":
                continue

            x, y = offset_x + dx, offset_y + dy
            if not (0 <= x < H and 0 <= y < W):
                return False, pre_grid
            if grid[x][y] == "#":
                return False, pre_grid

            grid[x][y] = "#"

    return True, grid


def pos(p):
    x, y = divmod(p, 2 * W)
    x -= H
    y -= W
    return x, y


def check(grid):
    for i in range(H):
        for j in range(W):
            if grid[i][j] == ".":
                return False
    return True


first_grid = [["."] * W for _ in range(H)]
M = (2 * H) * (2 * W)

for p1 in range(M):
    for p2 in range(M):
        for p3 in range(M):
            # 1つ目のミノを置く
            x1, y1 = pos(p1)
            x2, y2 = pos(p2)
            x3, y3 = pos(p3)

            # 回転の分
            minos = [P[0], P[1], P[2]]
            grids = [None] * 3
            for r1 in range(4):
                if r1 > 0:
                    minos[0] = rotate(minos[0])
                b, grids[0] = put(first_grid, minos[0], x1, y1)
                if not b:
                    continue
                for r2 in range(4):
                    if r2 > 0:
                        minos[1] = rotate(P[1])
                    b, grids[1] = put(grids[0], minos[1], x2, y2)
                    if not b:
                        continue
                    for r3 in range(4):
                        if r3 > 0:
                            minos[2] = rotate(minos[2])
                        minos[2] = rotate(minos[2])
                        b, grids[2] = put(grids[1], minos[2], x3, y3)
                        if not b:
                            continue

                        if check(grids[2]):
                            print("Yes")
                            exit()

print("No")
