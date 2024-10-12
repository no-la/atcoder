N = int(input())
A = [input() for _ in range(N)]

rotate_count = [[0] * N for _ in range(N)]
for i in range(N // 2):
    for j in range(i, N - i):
        c = (i + 1) % 4
        rotate_count[i][j] = c
        rotate_count[j][i] = c
        rotate_count[-i - 1][j] = c
        rotate_count[j][-i - 1] = c

# print(*rotate_count, sep="\n")


def rotate(i, j, n):
    """(i, j)をn回時計回りに回転する"""
    for _ in range(n):
        # i, j = j, N - i - 1
        i, j = N - j - 1, i
    return i, j


ans = [[None] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        ni, nj = rotate(i, j, rotate_count[i][j])
        ans[i][j] = A[ni][nj]

for l in ans:
    print(*l, sep="")
