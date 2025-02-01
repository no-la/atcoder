N, M = map(int, input().split())
S = [input() for _ in range(N)]
T = [input() for _ in range(M)]


def is_T(offset_i, offset_j):
    """(i, j)を右上として調べる"""
    if not (offset_i + M <= N and offset_j + M <= N):
        return False

    for i in range(M):
        for j in range(M):
            if S[offset_i + i][offset_j + j] != T[i][j]:
                return False
    return True


# N^2 * m^2
for i in range(N):
    for j in range(N):
        if is_T(i, j):
            print(i + 1, j + 1)
            exit()
