N = 9
S = [input() for _ in range(N)]
M = N**2


def check(x):
    i, j = divmod(x, N)
    return S[i][j] == "#"


def f(x, y):
    xi, xj = divmod(x, N)
    yi, yj = divmod(y, N)
    return (xi - yi) ** 2 + (xj - yj) ** 2


# 4点の全探索で正方形か調べる
ans = set()
for a in range(M):
    if not check(a):
        continue
    for b in range(M):
        if not check(b) or a == b:
            continue
        for c in range(M):
            ci, cj = divmod(c, N)
            if not check(c) or a == c or b == c:
                continue
            for d in range(M):
                di, dj = divmod(d, N)
                if not check(d) or a == d or b == d or c == d:
                    continue
                if len(set([a, b, c, d])) != 4:
                    continue
                if f(a, b) == f(b, c) == f(c, d) == f(d, a):
                    ans.add(tuple(sorted([a, b, c, d])))

print(len(ans))
