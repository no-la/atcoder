N, M = map(int, input().split())
X = list(map(int, input().split()))
A = list(map(int, input().split()))

if 1 not in X:
    print(-1)
    exit()

from collections import defaultdict

d = defaultdict(list)
# d[i]: マスiにある石の個数

for x, a in zip(X, A):
    d[x] = a

# print(d)

carrying = 0
ans = 0
bi = 1
for i in sorted(d.keys()):
    dist = i - bi
    ans += dist * (carrying + carrying - dist)
    carrying -= max(0, dist)

    if carrying < 0:
        print(-1)
        exit()

    carrying += d[i] - 1
    bi = i
    # print(i, carrying, ans, dist)

if bi < N:
    dist = N - bi
    ans += dist * (carrying + carrying - dist)

    if carrying < 0:
        print(-1)
        exit()

    carrying -= dist

print(ans if carrying == 0 else -1)
# print(ans, carrying)
