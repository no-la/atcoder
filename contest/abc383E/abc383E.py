N, M, K = map(int, input().split())
d = [[] for _ in range(N)]
for _ in range(M):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    d[u].append((v, w))
    d[v].append((u, w))
