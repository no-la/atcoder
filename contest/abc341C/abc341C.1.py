H, W, N = map(int, input().split())
T = input()
S = [input() for _ in range(H)]

ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j]=="#":
            continue
        pi = i
        pj = j
        for k in range(N):
            delta = None
            if T[k]=="L":
                delta = (0, -1)
            elif T[k]=="R":
                delta = (0, 1)
            elif T[k]=="U":
                delta = (-1, 0)
            else:
                delta = (1, 0)
            pi = pi+delta[0]
            pj = pj+delta[1]
            
            if S[pi][pj]=="#":
                break
        else:
            ans += 1
print(ans)