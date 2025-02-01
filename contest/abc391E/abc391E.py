N = int(input())
A = input()

d = [[0] * (3**i) for i in range(N + 1)]
# d[i][j]: N-i回操作後の左からj文字目
d[N] = list(map(int, A))
for i in range(N - 1, -1, -1):
    for j in range(0, 3**i):
        d[i][j] = int(sum(d[i + 1][3 * j : 3 * j + 3]) >= 2)


def f(i, j):
    """d[i][j]を変えるために必要な操作回数"""
    if i == N:
        return 1

    to = d[i][j] ^ 1
    temp = []
    for k in range(3 * j, 3 * j + 3):
        if d[i + 1][k] != to:
            temp.append(f(i + 1, k))

    if sum(d[i + 1][3 * j : 3 * j + 3]) in [1, 2]:
        return min(temp)
    else:
        return sum(sorted(temp)[:2])


print(f(0, 0))
