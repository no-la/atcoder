N, M = map(int, input().split())
X = list(map(int, input().split()))
A = list(map(int, input().split()))

from collections import defaultdict

d = defaultdict(int)
for i in range(M):
    x, a = X[i], A[i]
    d[x] = a
X = sorted(X)
ans = 0
count = 0
bi = 0
for i in X:
    need = i - bi - 1
    # print(bi, "->", i, need, count, d[i], ans)
    if count < need:
        print(-1)
        exit()
    if need == 0:
        ans += count
    else:
        ans += need * (2 * count - need + 1) // 2
    count -= need
    count += d[i] - 1
    bi = i

if i < N:
    need = N - i
    # print(need, count)
    ans += need * (count + count - need + 1) // 2
    count -= need


print(ans if count == 0 else -1)
