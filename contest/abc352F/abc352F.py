N, M = map(int, input().split())
A = [[None]*N for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    A[a-1][b-1] = c
    A[b-1][a-1] = -c



