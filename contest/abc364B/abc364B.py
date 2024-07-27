H, W = map(int, input().split())
S = list(map(lambda x: int(x)-1, input().split()))
C = [input() for _ in range(H)]
X = input()

pos = S
for i in range(len(X)):
    s = X[i]
    if s=="L":
        delta = (0, -1)
    elif s=="R":
        delta = (0, 1)
    elif s=="U":
        delta = (-1, 0)
    elif s=="D":
        delta = (1, 0)

    h, w = [pos[0]+delta[0], pos[1]+delta[1]]

    if 0<=h<H and 0<=w<W and C[h][w]==".":
        pos = [h, w]

print(pos[0]+1, pos[1]+1)
