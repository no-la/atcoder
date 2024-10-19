N, Q = map(int, input().split())
lr = [0, 1]

ans = 0
for _ in range(Q):
    h, t = input().split()
    t = int(t) - 1
    if h == "L":
        i = 0
    else:
        i = 1
    j = (i + 1) % 2

    a, b, c, d = [None] * 4
    # 左に
    if t - N <= lr[i] < lr[j]:
        a = lr[i] - (t - N)
    else:
        b = abs(lr[j] - (t - N) + 1) + abs(lr[i] - (t - N))

    # 右に
    if lr[i] < lr[j] < t:
        c = t - lr[j] + 1 + t - lr[i]
    else:
        d = abs(t - lr[i])

    print(lr, h, t, a, b, c, d)
    if b is not None and d is not None:
        if b < d:
            ans += b
            lr[i], lr[j] = t, (t - 1) % N
        else:
            ans += d
            lr[i] = t
    elif b is not None and c is not None:
        if b < c:
            ans += b
            lr[i], lr[j] = t, (t - 1) % N
        else:
            ans += c
            lr[i], lr[j] = t, (t + 1) % N
    elif a is not None and d is not None:
        if a < d:
            ans += a
            lr[i] = t
        else:
            ans += d
            lr[i] = t
    else:
        if a < c:
            ans += a
            lr[i] = t
        else:
            ans += c
            lr[i], lr[j] = t, (t + 1) % N


print(ans)
