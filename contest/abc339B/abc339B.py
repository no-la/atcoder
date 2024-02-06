H, W, N = map(int, input().split())
d = [[0, -1], [1, 0], [0, 1], [-1, 0]]

ans = [["."]*W for _ in range(H)]
pos = [0, 0]
e = 0 #向き
for _ in range(N):
    if ans[pos[1]][pos[0]]==".":
        ans[pos[1]][pos[0]] = "#"
        e = (e+1)%4
    else:
        ans[pos[1]][pos[0]] = "."
        e = (e-1)%4
    pos[0] = (pos[0] + d[e][0])%W
    pos[1] = (pos[1] + d[e][1])%H

print("\n".join(map(lambda l: "".join(l), ans)))