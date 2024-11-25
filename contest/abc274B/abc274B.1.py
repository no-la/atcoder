H, W = map(int, input().split())
C = [input() for _ in range(H)]

ans = [0] * W
for i in range(H):
    for j in range(W):
        ans[j] += C[i][j] == "#"

print(*ans)
