N, M, Q = map(int, input().split())
d = [tuple(map(int, input().split()[::-1])) for _ in range(N)]
d.sort(reverse=True)

X = list(map(int, input().split()))
X = [(x, i) for i, x in enumerate(X)]
X.sort()

for _ in range(Q):
    L, R = map(int, input().split())
    seen = set()
    ans = 0
    for x, i in X:
        if L <= i + 1 <= R:
            continue
        for j, vw in enumerate(d):
            if j in seen:
                continue
            v, w = vw
            if w <= x:
                ans += v
                seen.add(j)
                break
    print(ans)
    # print(seen)
