H, W = map(int, input().split())
S = [input() for _ in range(H)]

p = []
for i in range(H):
    for j in range(W):
        if S[i][j]=="o":
            p.append([i, j])

print(abs(p[0][0]-p[1][0])+abs(p[0][1]-p[1][1]))
