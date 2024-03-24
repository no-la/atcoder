H, W, K = map(int, input().split())
A = [input() for _ in range(H)]

ans = 0

# 全探索
# bit全探索
N = H+W
for i in range(2 ** N):
    lines = []
    columns = []
    for j in range(N):
        if not ((i >> j) & 1):
            continue
        # A[j]を選ぶ場合なので、適当な処理を書く
        if j<H:
            lines.append(j)
        else:
            columns.append(j-H)
    ans += sum([A[k//W][k%W]=="#" and 
        k//W not in lines and
        k%W not in columns for k in range(H*W)]) == K
print(ans)