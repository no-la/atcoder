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


def check(minos, x1, y1, x2, y2, x3, y3):
    """ミノを置けるか"""
    grid = [["."] * W for _ in range(H)]

    # ミノを置く
    for i, (offset_x, offset_y) in enumerate([(x1, y1), (x2, y2), (x3, y3)]):
        for dx in range(H):
            for dy in range(W):
                if minos[i][dx][dy] == ".":
                    continue

                x, y = offset_x + dx, offset_y + dy
                if not (0 <= x < H and 0 <= y < W):
                    return False
                if grid[x][y] == "#":
                    return False

                grid[x][y] = "#"

    # 全部"#"になっているか
    for i in range(H):
        for j in range(W):
            if grid[i][j] != "#":
                return False
    return True


def pos(p):
    x, y = divmod(p, 2 * W)
    x -= H
    y -= W
    return x, y


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
            for r1 in range(4):
                minos[0] = rotate(minos[0])
                for r2 in range(4):
                    minos[1] = rotate(minos[1])
                    for r3 in range(4):
                        minos[2] = rotate(minos[2])
                        if check(minos, x1, y1, x2, y2, x3, y3):
                            print("Yes")
                            exit()

print("No")
