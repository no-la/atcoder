H, W = map(int, input().split())
G = [input() for _ in range(H)]


i, j = 0, 0
seen = [[False]*W for _ in range(H)]
seen[0][0] = True
while True:
    s = G[i][j]
    if s=="L":
        delta = (0, -1)
    elif s=="R":
        delta = (0, 1)
    elif s=="U":
        delta = (-1, 0)
    elif s=="D":
        delta = (1, 0)
    
    i += delta[0]
    j += delta[1]
    if not (0<=i<H and 0<=j<W):
        print(i-delta[0]+1, j-delta[1]+1)
        exit()
    if seen[i][j]:
        print(-1)
        exit()
    seen[i][j] = True
    
