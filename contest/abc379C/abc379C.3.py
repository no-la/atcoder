N, M = map(int, input().split())
X = list(map(int, input().split()))
A = list(map(int, input().split()))

if 1 not in X:
    print(-1)
    exit()

from collections import defaultdict

d = defaultdict(int)
# d[i]: マスiにある石の個数

for x, a in zip(X, A):
    d[x] = a

d[N] = max(0, d[N])

keys = sorted(d.keys())
bi = 1
for i in keys[1:]:
    if d[bi] < i - 1:
        print(-1)
        exit()
    d[i] += d[bi]
    bi = i
    # print(i, d[i])

if d[N] != N:
    print(-1)
    exit()

ans = N * (N + 1) // 2 - sum([x * a for x, a in zip(X, A)])
print(ans)
