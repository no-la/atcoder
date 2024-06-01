N, M = map(int, input().split())
A = list(map(int, input().split()))
X = [list(map(int, input().split())) for _ in range(N)]

d = [0]*M
for i in range(N):
    for j in range(M):
        d[j] += X[i][j]

print("Yes" if all([d[i]>=A[i] for i in range(M)]) else "No")
