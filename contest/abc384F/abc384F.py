N = int(input())
A = list(map(int, input().split()))

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

    print(i, f"[{j}, {N}]", ans)

print("-" * 20)

# d[i][0]ごとにまとめて数える
seen = set()
for i in range(N):
    if d[i][0] in seen:
        continue
    seen.add(d[i][0])
    l = bisect.bisect_left(d, (d[i][0], 0))
    r = bisect.bisect_right(d, (d[i][0], INF))
    ans += (r - l) * (d[i][1] // (2 ** d[i][0])) + (cumsum[r] - cumsum[l]) // (
        2 ** (d[i][0] + 1)
    )
    print(i, f"[{l}, {r})", ans)

print(d)
print(cumsum)
print(ans)
