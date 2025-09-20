import sys

input = lambda: sys.stdin.readline().rstrip()
T = int(input())


def solve(H, W, S):
    ans = 0
    weight = [[0] * W for _ in range(H)]

    for i in range(H):
        for j in range(W):
            if not is_box(S, i, j):
                continue
            for s in range(i, i + 2):
                for t in range(j, j + 2):
                    weight[s][t] += 1

    nx = get_nx(weight)
    # print(*weight, sep="\n")
    # print("-" * 20)
    while nx is not None:
        i, j = nx
        ans += 1
        for s in range(i - 1, i + 1):
            for t in range(j - 1, j + 1):
                if not is_box(S, s, t):
                    continue
                for u in range(s, s + 2):
                    for v in range(t, t + 2):
                        weight[u][v] -= 1
        nx = get_nx(weight)
        # print(*weight, sep="\n")
        # print("-" * 20)
    print(ans)


def get_nx(weight):
    rev = None
    temp = 0
    for i in range(H):
        for j in range(W):
            if weight[i][j] > temp:
                temp = weight[i][j]
                rev = (i, j)
    return rev


def is_box(S, i, j):
    for s in range(i, i + 2):
        for t in range(j, j + 2):
            if not (0 <= s < H and 0 <= t < W):
                return False
            if S[s][t] == ".":
                return False
    return True


for _ in range(T):
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    solve(H, W, S)
