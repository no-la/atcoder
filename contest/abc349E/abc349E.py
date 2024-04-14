A = [list(map(int, input().split())) for _ in range(3)]

score_sum = sum(A)
# 全探索
# 9! = 3.6*10^5


win = [0, 0]

d = list(range(9))
# 順列 O(nPk)<=n!
import itertools
for l in itertools.permutations(d, 9):
    aoki = 0
    takahasi = 0
    grid = [[0]*3 for _ in range(3)] # 先行は1, 後攻は2
    for c, temp in enumerate(l):
        a, b = divmod(temp, 3)
        # 置くべき場場所を調べる
        # 次に負けないようにする
        cand = set()
        for i in range(3):
            if sum(grid[i])*(2-c%2)==2*(2-c%2):
                for j in range(3):
                    if grid[i][j]!=0:
                        cand.add((i, j))
        # 縦
        if not cand:
            for j in range(3):
                if sum([grid[i][j] for i in range(3)])==2:
                    for j in range(3):
                        if grid[i][j]!=0:
                            cand.add((i, j))
        # 斜め
        if not cand:
            for di, dj in [(1, 1), (1, -1)]:
                if sum([grid[di*i][dj*i] for i in range(3)])==2:
                    for i in range(3):
                        if grid[di*i][dj*i]!=0:
                            cand.add((di*i%3, dj*i%3))

        if (a, b) in cand:
            grid[a][b] = c%2+1
            if c%2==0:
                takahasi += A[a][b]
            else:
                aoki += A[a][b]
        else:
            break
    else:
        if takahasi>aoki:
            ...