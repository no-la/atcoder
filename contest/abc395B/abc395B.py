import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
d = [["." for _ in range(N)] for _ in range(N)]

for i in range(0, N, 2):
    for j in range(i, N - i):
        d[i][j] = "#"
    for j in range(i, N - i):
        d[j][i] = "#"
    for j in range(i, N - i):
        d[N - i - 1][j] = "#"
    for j in range(i, N - i):
        d[j][N - i - 1] = "#"

for l in d:
    print(*l, sep="")
