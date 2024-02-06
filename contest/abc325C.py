H, W = map(int, input().split())
S = [input() for i in range(H)]

ans = 0
seen = [False]*(H*W)
for i in range(H):
    for j in range(W):
        if S[i][j]=="#" and not seen[i*W+j]:
            ans += 1
            todo = [[i,j]]
            seen[i*W+j] = True
            while len(todo)!=0:
                v = todo.pop()
                for y in range(-1, 2):
                    for x in range(-1, 2):
                        k = v[0]+y
                        l = v[1]+x
                        if k<0 or H<=k or l<0 or W<=l:
                            continue
                        if not seen[k*W+l] and S[k][l]=="#":
                            todo.append([k, l])
                            seen[k*W+l] = True

print(ans)