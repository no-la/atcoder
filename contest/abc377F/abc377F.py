import bisect

N, M = map(int, input().split())
lines = []
columns = []
diagonal1 = []  # \
diagonal2 = []  # /

for _ in range(M):
    a, b = map(int, input().split())
    lines.append(a)
    columns.append(b)
    diagonal1.append(b - a)
    diagonal2.append(b + a)

lines = sorted(set(lines))
columns = sorted(set(columns))
diagonal1 = sorted(set(diagonal1))
diagonal2 = sorted(set(diagonal2))

ans = N**2
ans -= len(lines) * N
ans -= len(columns) * N
ans += M
# diagonals
for j in diagonal1:
    s = (1, j) if j >= 1 else (1 - j + 1, 1)
    g = (N - j + 1, N) if j >= 1 else (N, N + j - 1)
    lc = abs(bisect.bisect_right(lines, g[0]) - bisect.bisect_left(lines, s[0]))
    cc = abs(bisect.bisect_right(columns, g[1]) - bisect.bisect_left(columns, s[1]))
    ans -= abs(g[0] - s[0])
    ans += lc + cc - 2
for j in diagonal2:
    s = (1, j) if j <= N else (j - N, N)
    g = (j, 1) if j <= N else (N, j - N)
    lc = abs(bisect.bisect_right(lines, g[0]) - bisect.bisect_left(lines, s[0]))
    cc = abs(bisect.bisect_right(columns, g[1]) - bisect.bisect_left(columns, s[1]))
    ans -= abs(g[0] - s[0])
    ans += lc + cc - 2


# diagonal1とdiagonal2が重なる部分を取り除く
# M<=10^3なのでM^2見れる
...

print(ans)
print(lines, columns, diagonal1, diagonal2, sep="\n")
