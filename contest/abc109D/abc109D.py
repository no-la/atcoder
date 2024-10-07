"""WA"""

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]


# 奇数を2つ見つけて適切なルートで両方を偶数にする
ans = []
start = None
for i in range(H):
    for j in range(W):
        if A[i][j] % 2 == 0:
            continue
        if start is None:
            start = [i, j]
        else:
            goal = [i, j]
            ydir = 1 if start[0] < goal[0] else -1
            xdir = 1 if start[1] < goal[1] else -1
            for y in range(start[0], goal[0], ydir):
                ans.append([y, start[1], y + ydir, start[1]])
            for x in range(start[1], goal[1], xdir):
                ans.append([goal[0], x, goal[0], x + xdir])

            start = None

print(len(ans))
for l in ans:
    print(*list(map(lambda x: x + 1, l)))
