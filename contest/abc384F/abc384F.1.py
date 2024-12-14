N = int(input())
A = list(map(int, input().split()))
M = max(A) + 1
d = [None] * N
# d[i]: (A[i] の素因数分解における2の指数, A[i] の素因数分解における奇数部分)

for i in range(N):
    a = A[i]
    count = 0
    while a % 2 == 0:
        a //= 2
        count += 1
    d[i] = (count, A[i])

d.sort()

cumsum = [0] * (N + 1)
for i in range(N):
    cumsum[i + 1] = cumsum[i] + d[i][1]


import bisect

ans = 0
INF = 10**15
for i in range(N):
    # d[i][0] < d[j][0] なる j をまとめて数える
    j = bisect.bisect_right(d, (d[i][0], INF))
    ans += (N - j) * (d[i][1] // (2 ** d[i][0])) + (cumsum[N] - cumsum[j]) // (
        2 ** d[i][0]
    )


# d[i][0]ごとにまとめて数える

# 準備
b = [[] * M for _ in range(30)]
# b[i][j]: 2の指数がiで、奇数部分を2^(j+1で割った余りのlist

for di in range(N):
    i = d[di][0]
    r = d[di][1]
    for j in range(30):
        b[i][j] = r % (2 ** (j + 1))
    b[i].sort()

seen = set()
for di in range(N):
    if d[di][0] in seen:
        continue
    seen.add(d[di][0])
    i = d[di][0]
    for j in range(30):
        tar = 2 ** (j + 1) - d[di][1]
        l = bisect.bisect_left(b[i], tar)
        r = bisect.bisect_right(b[i], tar)
    ans += (r - l) * (d[di][1] // (2 ** d[di][0])) + (cumsum[r] - cumsum[l]) // (
        2 ** (d[di][0] + 1)
    )


print(ans)
