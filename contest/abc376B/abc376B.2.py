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

    if lr[i] == t:
        continue

    t1, t2 = sorted([t, t - N * (t - lr[i]) // abs(t - lr[i])])

    c1 = lr[i] - t1 + (lr[j] - t1 + 1 if t1 < lr[j] < lr[i] else 0)
    c2 = t2 - lr[i] + (t2 - lr[j] + 1 if lr[i] < lr[j] < t2 else 0)

    print(h, t, ":", t1, *lr, t2, f"{c1=}, {c2=}")
    if c1 < c2:
        ans += c1
        if t1 < lr[j] < lr[i]:
            lr[j] = (t1 - 1) % N
        lr[i] = t1 % N
    else:
        ans += c2
        if lr[i] < lr[j] < t2:
            lr[j] = (t2 + 1) % N
        lr[i] = t2 % N

print(ans)
