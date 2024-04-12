H, W, N, M = map(int, input().split())
d = [[0]*W for _ in range(H)]
for _ in range(N):
    a, b = map(lambda x: int(x)-1, input().split())
    d[a][b] = 1
for _ in range(M):
    c, e = map(lambda x: int(x)-1, input().split())
    d[c][e] = 2

# print("-"*10)
# print(*d, sep="\n")
# 行、列ごとに調べる
# 尺取り法 or 二分探索

ans = [[0]*W for _ in range(H)]
# 列
for j in range(W):
    # 尺取り法
    right = 0
    exists = False
    for left in range(H):
        if d[left][j]==2:
            right += 1
            continue
        while right<H and d[right][j]!=2: # 条件の判定
            exists = exists or d[right][j]==1
            right += 1
        if exists:
            for i in range(left, min(right, H)):
                ans[i][j] = 1
        # 初期化
        exists = False

# 行
for i in range(H):
    # 尺取り法
    right = 0
    exists = False
    for left in range(W):
        if d[i][left]==2:
            right += 1
            continue
        while right<W and d[i][right]!=2: # 条件の判定
            exists = exists or d[i][right]==1
            right += 1
        if exists:
            for j in range(left, min(right, W)):
                ans[i][j] = 1
        # 初期化
        exists = False
# print("-"*10)
# print(*ans, sep="\n")
print(sum([sum(w) for w in ans]))
