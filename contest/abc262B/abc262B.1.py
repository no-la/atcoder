N, M = map(int, input().split())
d = [[False]*(N+1) for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    d[u][v] = True
    d[v][u] = True

ans = 0
for a in range(1, N+1):
    for b in range(a+1, N+1):
        for c in range(b+1, N+1):
            if d[a][b] and d[b][c] and d[c][a]:
                ans += 1

print(ans)
