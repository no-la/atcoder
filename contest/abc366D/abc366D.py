N = int(input())
A = [[list(map(int, input().split())) for _ in range(N)] for _ in range(N)]
Q = int(input())

# 累積和？
d = [[[0]*(N+1) for _ in range(N+1)] for _ in range(N+1)]
for x in range(N):
    for y in range(N):
        for z in range(N):
            d[x+1][y+1][z+1] = (
                A[x][y][z]
                + d[x][y+1][z+1]
                + d[x+1][y][z+1]
                + d[x+1][y+1][z]
                - d[x][y+1][z]
                - d[x+1][y][z]
                - d[x][y][z+1]
                + d[x][y][z]
            )

for _ in range(Q):
    Lx, Rx, Ly, Ry, Lz, Rz = map(int, input().split())
    ans = (
        d[Rx][Ry][Rz]
        - d[Lx-1][Ry][Rz]
        - d[Rx][Ly-1][Rz]
        - d[Rx][Ry][Lz-1]
        + d[Lx-1][Ly-1][Rz]
        + d[Rx][Ly-1][Lz-1]
        + d[Lx-1][Ry][Lz-1]
        - d[Lx-1][Ly-1][Lz-1]
    )
    print(ans)
