N = int(input())
MG = int(input())
G = [[False]*N for _ in range(N)]
for _ in range(MG):
    u, v = map(lambda x: int(x)-1, input().split())
    G[u][v] = True
    G[v][u] = True
MH = int(input())
H = [[False]*N for _ in range(N)]
for _ in range(MH):
    u, v = map(lambda x: int(x)-1, input().split())
    H[u][v] = True
    H[v][u] = True

A = [list(map(int, input().split())) for _ in range(N-1)]


ans = 10**10
# 順列 O(nPk)<=n!
import itertools
for l in itertools.permutations(range(N), N):
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if G[l[i]][l[j]]!=H[i][j]:
                count += A[i][j-i-1]
                # print((i, j), (i, j-i-1))
    ans = min(ans, count)

print(ans)               
