A = [list(map(int, input().split())) for _ in range(3)]

score_sum = sum(A)
# 全探索
# 9C5 * 4 = 126 * 4 = 504

def rotate():
    A[0], A[2] = A[2], A[0]
    for i in range(3):
        for j in range(3):
            if i<j:
                A[i][j] = A[j][i]
            

d = list(range(9))
# 重複なし組み合わせ O(nCk)
import itertools
for _ in range(4): # for rotate
    for l in itertools.combinations(d, 4):
        grid = [[0]*3 for _ in range(3)]
        score = 0
        for p in l:
            i, j = divmod(p, 3)
            grid[i][j] = 1
            score += A[i][j]
        
        # 縦横斜め
        # 横
        ok = True
        for i in range(3):
            if sum([grid[i]])==3:
                ok = False
                break
        if not ok:
            continue
        # 縦
        for j in range(3):
            if sum([grid[i][j] for i in range(3)])==3:
                ok = False
                break
        if not ok:
            continue
        # 斜め
        for di, dj in [(1, 1), (1, -1)]:
            if sum([grid[di*i][dj*i] for i in range(3)])==3:
                ok = False
                break
        if not ok:
            continue

        aoki = max(aoki, score)
    rotate()