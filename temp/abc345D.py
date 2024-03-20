
N, H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# 使うタイルを見つける
D = []
S = H*W
# bit全探索
for i in range(2 ** N):
    temp = []
    for j in range(N):
        if not ((i >> j) & 1):
            continue
        # A[j]を選ぶ場合なので、適当な処理を書く
        temp.append(A[j])
    if sum([a*b for a, b in temp])==S:
        D.append(temp)

# 雑に全探索
M = [[0]*W for _ in range(H)]
def f(tiles):
    for i in range(H-tiles[0][1]):
        for j in range(W-tiles[0][0]):
            for x in range(i, i+tiles[-1][0]):
                for y in range(j, j+tiles[0][1]):
                    M[x][y] = 1
            f(tiles[1:])
            for x in range(i, i+tiles[-1][0]):
                for y in range(j, j+tiles[0][1]):
                    M[y][x] = 1
            f(tiles[1:])
