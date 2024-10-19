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

    lc = (t - lr[i]) % N
    rc = -lc % N

    if lr[i] + rc != t:
        lc, rc = rc, lc

    if lr[i] < lr[j] < t:
        lc += t - lr[j] + 1
