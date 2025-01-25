H, W = map(int, input().split())
S = [input() for _ in range(H)]

# 四隅を決めてその中を調べるイメージ

left = W
right = 0
up = H
down = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            left = min(left, j)
            right = max(right, j)
            up = min(up, i)
            down = max(down, i)


for i in range(H):
    for j in range(W):
        if S[i][j] == "." and up <= i <= down and left <= j <= right:
            print("No")
            exit()

print("Yes")
