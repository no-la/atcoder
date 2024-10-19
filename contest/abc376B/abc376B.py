N, Q = map(int, input().split())
l, r = 0, 1

ans = 0
for _ in range(Q):
    h, t = input().split()
    t = int(t) - 1
    if h == "L":
        a, b, c, d = [None] * 4
        # 左に
        if t - N <= l < r:
            a = l - (t - N)
        else:
            b = r - (t - N) + 1 + l - (t - N)

        # 右に
        if l < r < t:
            c = t - r + 1 + t - l
        else:
            d = t - l

        if a is None and c is None:
            if b < d:
                ans += b
                l, r = t, (t - 1) % N
            else:
                ans += d
                l = t
        elif a is None and d is None:
            if b < c:
                ans += b
                l, r = t, (t - 1) % N
            else:
                ans += c
                l, r = t, (t + 1) % N
        if b is None and c is None:
            if a < d:
                ans += a
                l = t
            else:
                ans += d
                l = t
        else:
            if a < c:
                ans += a
                l = t
            else:
                ans += c
                l, r = t, (t + 1) % N

print(ans)
