H, W, K = map(int, input().split())
S = [input() for _ in range(H)]

ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            continue
        dp = [[[0] * W for _ in range(H)] for _ in range(K + 1)]
        # dp[k][a][b]: (i,j)からk回移動して(a,b)に行く場合の数
        dp[0][i][j] = 1
        for k in range(K):
            for a in range(H):
                for b in range(W):
                    for da, db in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                        na, nb = a + da, b + db
                        if not (0 <= na < H and 0 <= nb < W):
                            continue
                        if S[na][nb] == "#":
                            continue
                        dp[k + 1][na][nb] += dp[k][a][b]
        # print(i, j, *dp)
        for a in range(H):
            for b in range(W):
                ans += dp[K][a][b]
print(ans)
