N = 3
M = 4
P = []

for i in range(N):
    P.append([list(input()) for j in range(M)])
print()

#右に90度回転
def rotate(mino):
    value = mino.copy()
    for i in range(M):
        mino[i] = value[M-1-i].copy()
    for i in range(M):
        for j in range(M):
            value[i][j] = mino[j][i]
    return value

#"#"の座標を一つ返す
def find_origin(mino):
    for i in range(M):
        for j in range(M):
            if mino[i][j] == "#":
                return [-i, -j]

def put_mino_at(grid_, mino, origin): #gridは(3*M)*(3*M)として外側の部分も用意しておく (0,0)↔(4,4)
    grid = [i.copy() for i in grid_]
    # print(grid_str(grid), grid_str(mino))
    for i in range(M):
        for j in range(M):
            #置こうとしている場所に既に置かれているorはみ出している
            if mino[i][j] == "#":
                if grid_[M+origin[0]+i][M+origin[1]+j] == "#":
                    # print(i, j, "duplicate")
                    return None
                elif origin[0]+i<0 or origin[0]+i>=M or origin[1]+j<0 or origin[1]+j>=M:
                    # print(i, j, "over")
                    return None
                else: #置けるので置く
                    grid[M+origin[0]+i][M+origin[1]+j] = "#"
    # print(grid_str(grid))
    #無事置けたのでgridを返す
    return grid

def judge_grid_full(grid):
    for i in range(M*M):
        if grid[M+i//M][M+i%M] ==".":
            return False
    return True

def grid_str(grid):
    ans = ""
    for i in range(len(grid)):
        ans += "".join(grid[i]) + "\n"
    return ans


P_0_BLOCK_POS = find_origin(P[0])

to_next = False
for i in range(M*M):
    grid = [["."]*(3*M) for i in range(3*M)]
    grid0 = put_mino_at(grid, P[0], [P_0_BLOCK_POS[0]+i//4, P_0_BLOCK_POS[1]+i%4])
    if grid0 == None:
        continue
    for k in range(4):
        P[1] = rotate(P[1])
        P_1_BLOCK_POS = find_origin(P[1])
        for j in range(M*M):
            grid1 = put_mino_at(grid0, P[1], [P_1_BLOCK_POS[0]+j//4, P_1_BLOCK_POS[1]+j%4])
            if grid1 ==  None:
                continue
            for m in range(4):
                P[2] = rotate(P[2])
                P_2_BLOCK_POS = find_origin(P[2])
                for l in range(M*M):
                    grid2 = put_mino_at(grid1, P[2], [P_2_BLOCK_POS[0]+l//4, P_2_BLOCK_POS[1]+l%4])
                    if grid2 != None and judge_grid_full(grid2):
                        print("Yes")
                        exit()
print("No")