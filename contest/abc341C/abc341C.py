H, W, N = map(int, input().split())
T = input()
S = [input() for _ in range(H)]

# 逆から見るので、上下左右逆にしておく
d = {"L":(0, 1), "R":(0, -1), "U":(1, 0), "D":(-1, 0)}
ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j]=="#":
            continue
        pi = i
        pj = j
        for k in range(N-1, -1, -1):
            pi = pi+d[T[k]][0]
            pj = pj+d[T[k]][1]
            if S[pi][pj]=="#":
                break
        else:
            ans += 1
print(ans)