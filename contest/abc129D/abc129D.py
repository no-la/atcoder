H, W = map(int, input().split())
S = [input() for _ in range(H)]


# 行、列ごとに尺取り法をするイメージ
count = [[0]*W for _ in range(H)]

# 行ごと
for i in range(H):
    l, r = 0, 0
    while l<W:
        if S[i][l]!=".":
            l += 1
            continue
        r = l+1
        while r<W and S[i][r]==".":
            r += 1
        
        for j in range(l, r):
            count[i][j] += r-l
        
        l = r+1

# 列ごと
for j in range(W):
    l, r = 0, 0
    while l<H:
        if S[l][j]!=".":
            l += 1
            continue
        r = l+1
        while r<H and S[r][j]==".":
            r += 1
        
        for i in range(l, r):
            if count[i][j]>0:
                count[i][j] -= 1 # (i,j)を重複して数えないようにする
            count[i][j] += r-l
        
        l = r+1

# print(*count, sep="\n")
ans = 0
for l in count:
    for v in l:
        ans = max(ans, v)

print(ans)
