N, M = map(int, input().split())
d = [[False]*N for _ in range(N)]
for _ in range(M):
    u, v = map(lambda x: int(x)-1, input().split())
    d[u][v] = True
    d[v][u] = True


ans = 0
for a in range(N):
    for b in range(a+1, N):
        if not d[a][b]:
            continue
        for c in range(b+1, N):
            if d[b][c] and d[a][c]:
                ans += 1
print(ans)

