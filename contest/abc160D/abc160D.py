N, X, Y = map(int, input().split())
X -= 1
Y -= 1

d = {i:[i+1] for i in range(N-1)}
d[N-1] = []
d[X].append(Y)
d[Y].append(X)

for k in range(1, N):
    ans = set()
    for i in range(N-k):
        left, right = i, i+k
        if abs(X-left)+1+abs(Y-right)<k:
            continue
        ans.add((left, right))
    for i in range(k):
        # xleft(xright) -> X -> Y -> yleft(yright)
        xleft, xright = X-i, X+i
        yleft, yright = Y-(k-i-1), Y+(k-i-1)
        for a in (xleft, xright):
            for b in (yleft, yright):
                if b-a<k:
                    continue
                if a<0 or b>N-1:
                    continue
                ans.add((a, b))
    print(len(ans))
    # print(ans)
